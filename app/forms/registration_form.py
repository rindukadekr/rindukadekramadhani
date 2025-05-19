from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Nama Lengkap', validators=[
        DataRequired(message="Nama lengkap wajib diisi."),
        Length(min=3, max=100, message="Nama harus memiliki 3-100 karakter.")
    ])
    email = StringField('Email', validators=[
        DataRequired(message="Email wajib diisi."),
        Email(message="Masukkan email yang valid.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Password wajib diisi."),
        Length(min=6, message="Password harus memiliki minimal 6 karakter.")
    ])
    confirm_password = PasswordField('Konfirmasi Password', validators=[
        DataRequired(message="Konfirmasi password wajib diisi."),
        EqualTo('password', message="Password dan konfirmasi password harus sama.")
    ])
    submit = SubmitField('Daftar')