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
from .static.predef_function.user_validation import UserValidation
from .static.predef_function.smt import Smt

auth: Blueprint = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login() -> dict:
    user_error: str = "Account Doesn't Exist"
    verification_error: str = "Please verify your account first"
    password_error: str = "Incorrect Password, Please try again!"
    success_response: str = "Logged in Succesfully"

    if request.method == "POST":

        user_credentials: dict = request.json
        user: User = User.query.filter_by(
            email=user_credentials["email"]).first()

        if not user:
            return jsonify({"error": user_error})

        if not user.confirmed:
            return jsonify({"error": verification_error})

        if not check_password_hash(user.password, user_credentials["password"]):
            return jsonify({"error": password_error})

        if verify_jwt_in_request(optional=True):
            valid_token = Tokens.query.filter_by(
                user_id=user.id).first()

            if valid_token:
                db.session.delete(valid_token)
                db.session.commit()

                jti = get_jwt()["jti"]
                now = datetime.now(timezone.utc)
                db.session.add(Tokenblocklist(jti=jti, created_at=now))
                db.session.commit()

        access_token: str = create_access_token(
            identity=user)

        user_token: Tokens = Tokens(
            data=access_token,
            user_id=user.id
        )

        db.session.add(user_token)
        db.session.commit()

        return jsonify({"success": success_response, "remembered": access_token})

    return jsonify({})


@auth.route("/resend", methods=["POST"])
def email_verification() -> dict:
    email_error: str = "Please Sign Up First!"
    email_existance_error: str = "Account doesn't Exist"
    success_response: str = "Email Already Confirmed!"

    if request.method == "POST":
        user_email: dict = request.json
        user_email: str = user_email["userEmail"]

        if not user_email:
            return jsonify({"error": email_error})

        stored_email: User = User.query.filter_by(email=user_email).first()

        if not stored_email:
            return jsonify({"error": email_existance_error})

        if stored_email.confirmed:
            return jsonify({"success": success_response})

        Smt(server=server, mail=mail, access="auth.confirm_email",
            data=user_email).send()

    return jsonify({})


@auth.route("/signup", methods=["POST"])
def signup() -> dict:
    captcha_validity_error: str = "Please Verify that you are not a Robot first!"
    duplicate_email_error: str = "Email Already Exist!, Please try another one."
    insertion_error: str = "Sorry, something went wrong!. Please try again."
    success_message: str = "Account Created Succesfully. A Verification Link has been sent to your Email."

    if request.method == "POST":
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

        try:
            new_user: User = User(
                user_name=user_credentials["name"],
                email=user_email,
                confirmed=False,
                password=generate_password_hash(
                    user_credentials["password"], method="pbkdf2:sha256")
            )

            db.session.add(new_user)
            db.session.commit()

            Smt(server=server, mail=mail, access="auth.confirm_email",
                data=user_email).send()
            return jsonify({"success": success_message})
        except Exception:
            return jsonify({"error": insertion_error})

    return jsonify({})


@auth.route("/email_confirmation", methods=["POST"])
def email_confirmation() -> dict:
    if request.method == "POST":
        user_email: dict = request.json
        user: User = User.query.filter_by(email=user_email).first()

        if not user:
            return jsonify({})

        confirmed: bool | int = user.confirmed

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
            token_url: str = confirm_serializer.loads(
                token, salt=server.config['SECURITY_PASSWORD_SALT'], max_age=3600)
        except Exception:
            return render_template("confirmation_template.html",
                                   content={
                                       "content": "The confirmation link is expired, or invalid token! ❌",
                                       "color": "crimson"
                                   })

        if not isinstance(token_url, str):
            return redirect(f"http://127.0.0.1:5000/index/{token}")

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
