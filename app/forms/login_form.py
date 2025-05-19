from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message="Email wajib diisi."),
        Email(message="Masukkan email yang valid.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Password wajib diisi."),
        Length(min=6, message="Password harus memiliki minimal 6 karakter.")
    ])
    submit = SubmitField('Login')