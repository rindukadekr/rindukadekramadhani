from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Registrasi, Formulir, db, Payment
from flask_login import login_user, login_required, current_user
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = Registrasi.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash('Login berhasil!', 'success')
            return redirect(url_for('main.home'))
        else:
            flash('Nama pengguna atau kata sandi salah.', 'danger')
    return render_template('login.html')

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash('Nama pengguna dan kata sandi wajib diisi.', 'danger')
            return redirect(url_for('main.register'))
        if Registrasi.query.filter_by(username=username).first():
            flash('Nama pengguna sudah terdaftar.', 'danger')
            return redirect(url_for('main.register'))
        new_user = Registrasi(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('Pendaftaran berhasil! Silakan lengkapi verifikasi siswa.', 'success')
        # Redirect langsung ke halaman verifikasi siswa
        return redirect(url_for('main.verifikasi_siswa'))
    return render_template('register.html')

@main_bp.route('/verifikasi_siswa', methods=['GET', 'POST'])
@login_required
def verifikasi_siswa():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        birth_date_str = request.form.get('birth_date')
        school_origin = request.form.get('school_origin')
        major = request.form.get('major')
        foto_ijazah = request.files.get('foto_ijazah')

        # Convert birth_date string to Python date object
        from datetime import datetime
        try:
            birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d').date()
        except Exception:
            flash('Format tanggal lahir tidak valid.', 'danger')
            return redirect(url_for('main.verifikasi_siswa'))

        # Simpan data ke Formulir
        filename = None
        if foto_ijazah:
            from werkzeug.utils import secure_filename
            import os
            UPLOAD_FOLDER = 'c:/Users/user/Documents/ppdb sederhana/uploads'
            filename = secure_filename(foto_ijazah.filename)
            foto_ijazah.save(os.path.join(UPLOAD_FOLDER, filename))

        new_formulir = Formulir(
            user_id=current_user.id,
            name=name,
            email=email,
            phone=phone,
            address=address,
            birth_date=birth_date,
            school_origin=school_origin,
            major=major,
            foto_ijazah=filename
        )
        db.session.add(new_formulir)
        db.session.commit()
        flash('Data verifikasi berhasil dikirim. Silakan menunggu persetujuan admin.', 'info')
        return redirect(url_for('main.verifikasi_selesai'))
    return render_template('verifikasi_siswa.html', user=current_user)

@main_bp.route('/verifikasi_selesai')
@login_required
def verifikasi_selesai():
    return render_template('verifikasi_selesai.html', user=current_user)

@main_bp.route('/uploads/<filename>')
def uploaded_file(filename):
    import os
    from flask import send_from_directory
    UPLOAD_FOLDER = 'c:/Users/user/Documents/ppdb sederhana/uploads'
    return send_from_directory(UPLOAD_FOLDER, filename)

@main_bp.route('/pembayaran', methods=['GET', 'POST'])
@login_required
def pembayaran():
    # Pastikan hanya siswa yang sudah diterima yang bisa akses pembayaran
    form = Formulir.query.filter_by(user_id=current_user.id).first()
    if not form or form.status != "Accepted":
        flash('Anda belum diterima oleh admin. Tunggu pemberitahuan lebih lanjut.', 'danger')
        return redirect(url_for('main.verifikasi_selesai'))
    if request.method == 'POST':
        payment_method = request.form.get('payment_method')
        amount = request.form.get('amount')
        # Simpan pembayaran ke database
        new_payment = Payment(
            user_id=current_user.id,
            payment_method=payment_method,
            amount=float(amount),
            created_at=datetime.utcnow()
        )
        db.session.add(new_payment)
        db.session.commit()
        flash('Pembayaran berhasil!', 'success')
        return redirect(url_for('main.home'))
    return render_template('pembayaran.html', user=current_user, form=form)

@main_bp.route('/rejection_notification')
@login_required
def rejection_notification():
    # Fetch the current user's form data
    form = Formulir.query.filter_by(user_id=current_user.id).first()
    if not form or form.status != "Rejected":
        flash('Anda tidak memiliki notifikasi penolakan.', 'info')
        return redirect(url_for('main.home'))
    return render_template('rejection_notification.html', user=current_user, form=form)

@main_bp.route('/sekolah_info')
def sekolah_info():
    return render_template('sekolah_info.html')