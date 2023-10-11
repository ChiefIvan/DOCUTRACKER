from . import db
from sqlalchemy import func


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    last_password_reset_request = db.Column(db.DateTime, default=None)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    full_verified = db.Column(db.Boolean, nullable=False, default=False)
    template_access = db.relationship("Template")
    credential_access = db.relationship("Credentials")
    document_access = db.relationship("Documents")


class Credentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_img = db.Column(db.String(2000), nullable=False)
    firstname = db.Column(db.String(20), nullable=False)
    mid_init = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    full_veri_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Documents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doc_reg_at = db.Column(db.DateTime(timezone=True), default=func.now())
    code = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    access = db.Column(db.Boolean, nullable=False, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Captcha(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(120), nullable=False)
    value = db.Column(db.String(5), nullable=False)


class Revoked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(100), nullable=False, index=True)
    revoked_at = db.Column(db.DateTime(timezone=True), nullable=False)


class Resend(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(120), nullable=False)


class Reset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(120), nullable=False)
