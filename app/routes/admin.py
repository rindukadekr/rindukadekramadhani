from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Registrasi, Formulir, Payment
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    # Ambil SEMUA data sesuai kebutuhan
    pending_students = Formulir.query.filter_by(status="Pending").all()
    accepted_students = Formulir.query.filter_by(status="Accepted").all()
    rejected_students = Formulir.query.filter_by(status="Rejected").all()
    paid_students = Payment.query.all()  # Atau join jika ingin detail

    return render_template(
        'admin_dashboard.html',
        user=current_user,
        pending_students=pending_students,
        accepted_students=accepted_students,
        rejected_students=rejected_students,
        paid_students=paid_students
    )

@admin_bp.route('/accept/<int:form_id>')
@login_required
def accept_registration(form_id):
    form = Formulir.query.get_or_404(form_id)
    form.status = "Accepted"
    db.session.commit()
    flash(f"Pendaftaran {form.name} telah diterima. Peserta dapat melanjutkan ke pembayaran.", "success")
    # Redirect ke halaman pembayaran untuk user yang bersangkutan
    if current_user.id == form.user_id:
        return redirect(url_for('main.pembayaran'))
    else:
        # Jika admin menerima pendaftaran milik user lain, tetap redirect ke dashboard admin
        return redirect(url_for('admin.dashboard'))

@admin_bp.route('/reject/<int:form_id>')
@login_required
def reject_registration(form_id):
    form = Formulir.query.get_or_404(form_id)
    form.status = "Rejected"
    db.session.commit()
    flash(f"Pendaftaran {form.name} telah ditolak.", "danger")
    # Redirect ke halaman notifikasi penolakan untuk user yang bersangkutan
    if current_user.id == form.user_id:
        return redirect(url_for('main.rejection_notification'))
    return redirect(url_for('admin.dashboard'))

@admin_bp.route('/delete/<int:form_id>', methods=['POST'])
@login_required
def delete_registration(form_id):
    form = Formulir.query.get_or_404(form_id)
    db.session.delete(form)
    db.session.commit()
    flash(f"Data pendaftar {form.name} berhasil dihapus.", "success")
    return redirect(url_for('admin.dashboard'))
