from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    last_password_reset_request = db.Column(db.DateTime, default=None)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)


class Captcha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(120), nullable=False)
    value = db.Column(db.String(5), nullable=False)


class Revoked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(100), nullable=False, index=True)
    revoked_at = db.Column(db.DateTime, nullable=False)
