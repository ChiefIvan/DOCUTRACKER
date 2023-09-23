from flask import (Blueprint, jsonify, request, render_template, redirect)
from flask_jwt_extended import create_access_token, get_jwt, verify_jwt_in_request

from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from time import sleep
from datetime import datetime, timezone
from captcha.image import ImageCaptcha
from io import BytesIO
from base64 import b64encode
from string import ascii_letters, digits
from random import choice
from uuid import uuid4

from . import (db, mail, server)
from .models import User, Tokens, Tokenblocklist, Captcha
from .static.predef_function.Validation import Validated
from .static.predef_function.Smt import Smt

auth: Blueprint = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login() -> dict:
    user_existance_error: str = "Account Doesn't Exist"
    Login_message: str = "Logged in succesfully"
    incorrect_password_error: str = "Incorrect password, please try again!"
    verification_error: str = "Please verify your account first"

    if request.method == "POST":

        login_user_credentials: dict = request.json
        user_existance: User = User.query.filter_by(
            email=login_user_credentials["email"]).first()

        if not user_existance:
            return jsonify({"error": user_existance_error})

        if not user_existance.confirmed:
            return jsonify({"error": verification_error})

        if not check_password_hash(user_existance.password, login_user_credentials["password"]):
            return jsonify({"error": incorrect_password_error})

        if verify_jwt_in_request(optional=True):
            valid_token = Tokens.query.filter_by(
                user_id=user_existance.id).first()

            if valid_token:
                db.session.delete(valid_token)
                db.session.commit()

                jti = get_jwt()["jti"]
                now = datetime.now(timezone.utc)
                db.session.add(Tokenblocklist(jti=jti, created_at=now))
                db.session.commit()

        access_token: str = create_access_token(
            identity=user_existance)

        user_token: Tokens = Tokens(
            data=access_token,
            user_id=user_existance.id
        )

        db.session.add(user_token)
        db.session.commit()

        return jsonify({"success": Login_message, "remembered": access_token})

    return jsonify({})


@auth.route("/resend", methods=["POST"])
def email_verification():
    unknown_email_message: str = "Please Sign Up First!"
    email_existance_error: str = "Account Doesn't Exist"
    email_confirmed_message: str = "Email Already Confirmed!"

    if request.method == "POST":
        user_email: dict = request.json
        user_email = user_email["userEmail"]
        if not user_email:
            return jsonify({"error": unknown_email_message})

        email_exist: User = User.query.filter_by(email=user_email).first()
        if not email_exist:
            return jsonify({"error": email_existance_error})

        if email_exist.confirmed:
            return jsonify({"success": email_confirmed_message})

        Smt(server=server, mail=mail, access="auth.confirm_email",
            data=user_email).send()

    return jsonify({})


@auth.route("/signup", methods=["POST"])
def signup() -> dict:
    database_insertion_error: str = "Sorry, something went wrong!. Please try again."
    success_message: str = "Account created succesfully. A verification link has been sent to your email."
    duplicate_error_message: str = "Email already exist!"
    captcha_validity_message: str = "Please verify that you are not a robot first!"

    if request.method == "POST":
        signup_user_credentials: dict = request.json

        if not signup_user_credentials["captVerification"]:
            return jsonify({"error": captcha_validity_message})

        signup_user_credentials |= {"captVerification": None}
        user_email: str = signup_user_credentials["email"]

        validated: bool | dict = Validated(signup_user_credentials).valid()

        if isinstance(validated, dict):
            return jsonify(validated)

        user_existance: User = User.query.filter_by(
            email=user_email).first()

        if user_existance:
            return jsonify({"error": duplicate_error_message})

        try:
            users: User = User(
                user_name=signup_user_credentials["name"],
                email=user_email,
                confirmed=False,
                password=generate_password_hash(
                    signup_user_credentials["password"], method="pbkdf2:sha256")
            )

            db.session.add(users)
            db.session.commit()

            Smt(server=server, mail=mail, access="auth.confirm_email",
                data=user_email).send()
            return jsonify({"success": success_message})
        except Exception:
            return jsonify({"error": database_insertion_error})

    return jsonify({})


@auth.route("/email_confirmation", methonds=["POST"])
def email_confirmation() -> dict:
    if request.method == "POST":
        user_email = request.json
        user_confirmed: User = User.query.filter_by(email=user_email).first()

        if not user_confirmed:
            return jsonify({})

        confirmed: bool | int = user_confirmed.confirmed

        if not confirmed:
            return jsonify({})

        return jsonify({})

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
        base64_data: str = b64encode(data.read()).decode("ascii")

        storing_captcha: Captcha = Captcha(
            identifier=identifier,
            value=text
        )

        db.session.add(storing_captcha)
        db.session.commit()

        return jsonify({
            "captcha": [base64_data, identifier],
            "Content-Type": "image/jpeg"
        })

    if request.method == "POST":
        user_capt_data: dict = request.json
        capt_id: str = user_capt_data["captchaId"]
        stored_captcha: Captcha = Captcha.query.filter_by(
            identifier=capt_id).first()

        if not stored_captcha:
            return jsonify({"error": False})

        if capt_id != stored_captcha.identifier:
            db.session.delete(stored_captcha)
            db.session.commit()
            return jsonify({"error": False})

        if user_capt_data["captValue"] != stored_captcha.value:
            db.session.delete(stored_captcha)
            db.session.commit()
            return jsonify({"error": False})

        db.session.delete(stored_captcha)
        db.session.commit()

        return jsonify({"success": True})

    return jsonify({})


@auth.route("/logout", methods=["GET"])
def logout():
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    db.session.add(Tokenblocklist(jti=jti, created_at=now))
    db.session.commit()
    return jsonify({})


@auth.route("/resetpassword", methods=["POST"])
def reset_password():
    user_existance_error: str = "Account Doesn't Exist"
    change_duration_message: str = "You can only change your password once every 7 days"

    reset_user_credentials: dict = request.json
    user_existance: bool = User.query.filter_by(
        email=reset_user_credentials["email"]).first()

    if not user_existance:
        return jsonify({"error": user_existance_error})

    return jsonify({})


@auth.route('/verification/<token>', methods=['GET'])
def confirm_email(token):
    if request.method == "GET":
        try:
            confirm_serializer: URLSafeTimedSerializer = URLSafeTimedSerializer(
                server.config['SECRET_KEY'])
            email: str = confirm_serializer.loads(
                token, salt=server.config['SECURITY_PASSWORD_SALT'], max_age=3600)
        except Exception:
            return render_template("confirmation_template.html",
                                   content={
                                       "content": "The confirmation link is expired, or invalid token! ❌",
                                       "color": "crimson"
                                   })

        if not isinstance(email, str):
            return redirect(f"http://127.0.0.1:5000/index/{token}")

        user: User = User.query.filter_by(email=email).first()

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
