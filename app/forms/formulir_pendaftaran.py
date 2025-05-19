from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class FormulirPendaftaranForm(FlaskForm):
    name = StringField('Nama Lengkap', validators=[
        DataRequired(message="Nama lengkap wajib diisi."),
        Length(min=3, max=100, message="Nama harus memiliki 3-100 karakter.")
    ])
    email = StringField('Email', validators=[
        DataRequired(message="Email wajib diisi."),
        Email(message="Masukkan email yang valid.")
    ])
    phone = StringField('Nomor Telepon', validators=[
        DataRequired(message="Nomor telepon wajib diisi."),
        Length(min=10, max=15, message="Nomor telepon harus valid.")
    ])
    address = TextAreaField('Alamat', validators=[
        DataRequired(message="Alamat wajib diisi.")
    ])
    birth_date = DateField('Tanggal Lahir', validators=[
        DataRequired(message="Tanggal lahir wajib diisi.")
    ])
    submit = SubmitField('Kirim Formulir')