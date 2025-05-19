from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Registrasi, db
from flask_login import login_user, login_required, current_user

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
        return redirect(url_for('main.verifikasi_siswa'))
    return render_template('register.html')

@main_bp.route('/verifikasi_siswa')
@login_required
def verifikasi_siswa():
    return render_template('verifikasi_siswa.html', user=current_user)