from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    verified = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Registrasi(UserMixin, db.Model):
    __tablename__ = 'registrasi'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Field to identify admin users

    def set_password(self, password):
        self.password = generate_password_hash(password)  # Hash the password

    def check_password(self, password):
        return check_password_hash(self.password, password)  # Verify the hashed password

    def __repr__(self):
        return f"<Registrasi {self.username}>"

class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('registrasi.id'), nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)

class Formulir(db.Model):
    __tablename__ = 'formulir'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('registrasi.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.Text, nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    school_origin = db.Column(db.String(100), nullable=False)
    major = db.Column(db.String(100), nullable=False)  # New field for major selection
    foto_ijazah = db.Column(db.String(200), nullable=True)  # Field for diploma photo
    status = db.Column(db.String(20), default="Pending")  # New field for registration status
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Formulir {self.name}>"

class Payment(db.Model):
    __tablename__ = 'payment'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('registrasi.id'), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Payment {self.user_id} - {self.amount}>"