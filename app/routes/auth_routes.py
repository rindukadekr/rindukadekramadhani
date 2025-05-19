from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.forms.registration_form import RegistrationForm
from app.forms.formulir_pendaftaran import FormulirPendaftaranForm
from app.models import Registrasi, Formulir
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.formulir'))  # Redirect ke formulir jika sudah login

    form = RegistrationForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = Registrasi.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            user.last_login = datetime.utcnow()
            db.session.commit()
            flash("Login berhasil! Silakan isi formulir pendaftaran.", "success")
            return redirect(url_for('auth.formulir'))  # Redirect ke formulir
        else:
            flash("Email atau password salah.", "danger")
    return render_template('login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Periksa apakah email sudah terdaftar
        existing_user = Registrasi.query.filter_by(email=email).first()
        if existing_user:
            flash("Email sudah terdaftar. Silakan gunakan email lain.", "danger")
            return redirect(url_for('auth.register'))

        # Simpan pengguna baru ke database
        new_user = Registrasi(
            name=name,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Pendaftaran berhasil! Silakan login untuk melanjutkan.", "success")
        return redirect(url_for('auth.formulir'))  # Redirect ke formulir

    return render_template('register.html', form=form)

@auth_bp.route('/formulir', methods=['GET', 'POST'])
@login_required
def formulir():
    form = FormulirPendaftaranForm()
    if form.validate_on_submit():
        # Simpan data formulir ke database
        new_form = Formulir(
            user_id=current_user.id,
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            address=form.address.data,
            birth_date=form.birth_date.data
        )
        db.session.add(new_form)
        db.session.commit()
        flash("Formulir pendaftaran berhasil disimpan!", "success")
        return redirect(url_for('main.home'))  # Redirect ke halaman utama

    return render_template('formulir_pendaftaran.html', form=form)