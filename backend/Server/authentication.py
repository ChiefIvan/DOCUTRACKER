from flask import Blueprint, jsonify, request, render_template, redirect, flash, url_for
from flask_jwt_extended import create_access_token, get_jwt, verify_jwt_in_request

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from datetime import datetime, timezone, timedelta
from captcha.image import ImageCaptcha
from io import BytesIO
from base64 import b64encode
from string import ascii_letters, digits
from random import choice
from uuid import uuid4

from . import db, mail, server
from .models import User, Captcha
from .static.predef_function.user_validation import UserValidation, PasswordValidator
from .static.predef_function.smt import Smt

auth: Blueprint = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login() -> dict:
    if request.method == "POST":

        user_error: str = "Account Doesn't Exist!"
        verification_error: str = "Please verify your account first!"
        password_error: str = "Incorrect Password, Please try again!"
        success_response: str = "Logged in Succesfully"

        user_credentials: dict = request.json
        user: User = User.query.filter_by(
            email=user_credentials["email"]).first()

        if not user:
            return jsonify({"error": user_error})

        if not user.confirmed:
            return jsonify({"error": verification_error})

        if not check_password_hash(user.password, user_credentials["password"]):
            return jsonify({"error": password_error})

        access_token: str = create_access_token(
            identity=user)

        return jsonify({"success": success_response, "remembered": access_token})

    return jsonify({})


@auth.route("/resend", methods=["POST"])
def email_verification() -> dict:
    if request.method == "POST":

        email_error: str = "Please Sign Up First!"
        email_existance_error: str = "Account doesn't Exist"
        success_response: str = "Email Already Confirmed!"

        user_email: dict = request.json
        user_email: str = user_email["userEmail"]

        if not user_email:
            return jsonify({"error": email_error})

        user: User = User.query.filter_by(email=user_email).first()

        if not user:
            return jsonify({"error": email_existance_error})

        if user.confirmed:
            return jsonify({"success": success_response})

        smt: Smt = Smt(server=server, mail=mail, access="auth.confirm_email",
                       data=user_email, username=user.user_name).send()

        if isinstance(smt, dict):
            return jsonify(smt)

        return jsonify({"response": True})

    return jsonify({})


@auth.route("/signup", methods=["POST"])
def signup() -> dict:
    if request.method == "POST":
        captcha_validity_error: str = "Please Verify that you are not a Robot first!"
        duplicate_email_error: str = "Email Already Exist!, Please try another one."
        insertion_error: str = "Sorry, something went wrong!. Please try again."
        success_message: str = "Account Created Succesfully. A Verification Link has been sent to your Email."

        user_credentials: dict = request.json

        if not user_credentials["captVerification"]:
            return jsonify({"error": captcha_validity_error})

        user_credentials |= {"captVerification": None}
        user_email: str = user_credentials["email"]

        validation_response: bool | dict = UserValidation(
            user_credentials).validate_user()

        if isinstance(validation_response, dict):
            return jsonify(validation_response)

        user: User = User.query.filter_by(
            email=user_email).first()

        if user:
            return jsonify({"error": duplicate_email_error})

        smt: Smt = Smt(server=server, mail=mail, access="auth.confirm_email",
                       data=user_email, username=user_credentials["name"]).send()

        if isinstance(smt, dict):
            return jsonify(smt)

        try:
            new_user: User = User(
                user_name=user_credentials["name"],
                email=user_email,
                confirmed=False,
                last_password_reset_request=None,
                password=generate_password_hash(
                    user_credentials["password"], method="pbkdf2:sha256")
            )

            db.session.add(new_user)
            db.session.commit()

            return jsonify({"success": success_message})
        except Exception:
            return jsonify({"error": insertion_error})

    return jsonify({})


@auth.route("/confirmed_check", methods=["POST"])
def check() -> dict:
    if request.method == "POST":
        user_email: dict = request.json
        user_email: str = user_email["userEmail"]
        user: User = User.query.filter_by(email=user_email).first()

        if not user:
            return jsonify({"response": True})

        confirmed: bool | int = user.confirmed

        if not confirmed:
            return jsonify({"response": False})

        return jsonify({"response": True})

    return jsonify({})


@auth.route("/captcha", methods=["GET", "POST"])
def captcha_verification():
    if request.method == "GET":
        text: str = ""
        identifier = str(uuid4())

        for _ in range(5):
            text += choice(ascii_letters + digits)

        captcha: ImageCaptcha = ImageCaptcha(
            width=400, height=220, font_sizes=(40, 60, 80, 100))
        data: BytesIO = captcha.generate(text)
        base64_image_data: str = b64encode(data.read()).decode("ascii")

        new_captcha: Captcha = Captcha(
            identifier=identifier,
            value=text
        )

        db.session.add(new_captcha)
        db.session.commit()

        return jsonify({
            "captcha": [base64_image_data, identifier],
            "Content-Type": "image/jpeg"
        })

    if request.method == "POST":
        captcha_data: dict = request.json
        captcha_id: str = captcha_data["captchaId"]
        stored_captcha: Captcha = Captcha.query.filter_by(
            identifier=captcha_id).first()

        if not stored_captcha:
            return jsonify({"error": False})

        if captcha_id != stored_captcha.identifier:
            db.session.delete(stored_captcha)
            db.session.commit()
            return jsonify({"error": False})

        if captcha_data["captValue"] != stored_captcha.value:
            db.session.delete(stored_captcha)
            db.session.commit()
            return jsonify({"error": False})

        db.session.delete(stored_captcha)
        db.session.commit()

        return jsonify({"success": True})

    return jsonify({})


# @auth.route("/logout", methods=["GET"])
# def logout():
#     jti = get_jwt()["jti"]
#     now = datetime.now(timezone.utc)
#     db.session.add(Tokenblocklist(jti=jti, created_at=now))
#     db.session.commit()
#     return jsonify({})


@auth.route("/reset", methods=["POST"])
def pswd_reset_req() -> dict:
    if request.method == "POST":
        user_error: str = "Account Doesn't Exist!"
        duration_mgs: str = "You can only change your password once every 7 days"
        request_msg: str = "A Reset Link has been sent to your Email."

        user_credentials: dict = request.json
        user: User = User.query.filter_by(
            email=user_credentials["email"]).first()

        if not user:
            return jsonify({"error": user_error})

        # if user.last_password_reset_request and \
        #         user.last_password_reset_request > datetime.utcnow() - timedelta(days=7):
        #     return jsonify({"error": duration_mgs})

        smt: Smt = Smt(server=server, mail=mail, access="auth.pswd_reset_confirm",
                       data=user.email, username=user.user_name).request()

        if isinstance(smt, dict):
            return jsonify(smt)

        user.last_password_reset_request = datetime.utcnow()
        db.session.commit()

        return jsonify({"success": request_msg})

    return jsonify({})


@auth.route("/confirm_reset/<token>", methods=["GET", "POST"])
def pswd_reset_confirm(token):
    try:
        confirm_serializer: URLSafeTimedSerializer = URLSafeTimedSerializer(
            server.config['SECRET_KEY'])
        token_url: str = confirm_serializer.loads(
            token, salt=server.config['SECURITY_PASSWORD_SALT'], max_age=15000)
    except Exception:
        return render_template("confirmation_template.html",
                               content={
                                   "content": "The confirmation link has expired, or invalid token! ❌",
                                   "color": "crimson"
                               })

    if request.method == "POST":
        new_password: str = request.form.get("password")
        cnfrm_password: str = request.form.get("cnfrm-password")
        user_passwords: str = {"password": new_password,
                               "confirm_password": cnfrm_password}
        validity: bool | dict = PasswordValidator(user_passwords).validate()

        if isinstance(validity, dict):
            flash(validity, category="error")
            return redirect(url_for("auth.pswd_reset_confirm", token=token))

        user: User = User.query.filter_by(email=token_url).first()

        if user:
            user.password = generate_password_hash(
                new_password, method="pbkdf2:sha256")
            db.session.commit()

            return render_template("confirmation_template.html",
                                   content={
                                       "content": "You change your password succesfully ✅",
                                       "color": "green"
                                   })

        flash("No user assciated with the token", category="error")
    return render_template("reset_form.html")


@auth.route("/verification/<token>", methods=['GET'])
def confirm_email(token):
    if request.method == "GET":
        try:
            confirm_serializer: URLSafeTimedSerializer = URLSafeTimedSerializer(
                server.config['SECRET_KEY'])
            token_url: str = confirm_serializer.loads(
                token, salt=server.config['SECURITY_PASSWORD_SALT'], max_age=3600)
        except Exception:
            return render_template("confirmation_template.html",
                                   content={
                                       "content": "The confirmation link has expired, or invalid token! ❌",
                                       "color": "crimson"
                                   })

        user: User = User.query.filter_by(email=token_url).first()

        if user.confirmed:
            return render_template("confirmation_template.html",
                                   content={
                                       "content": "Email already confirmed ✅",
                                       "color": "green"
                                   })

        else:
            user.confirmed = True
            db.session.add(user)
            db.session.commit()
            return render_template("confirmation_template.html",
                                   content={
                                       "content": "Email confirmed ✅",
                                       "color": "green"
                                   })
