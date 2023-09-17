from flask import (Blueprint, jsonify, request, render_template, redirect)
from flask_jwt_extended import create_access_token, get_jwt, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from time import sleep
from datetime import datetime, timezone

from . import (db, mail, server)
from .models import User, Tokens,  Tokenblocklist
from .static.predef_function.Validation import Validated
from .static.predef_function.Smt import Smt

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login() -> dict:
    user_existance_error: str = "Account Doesn't Exist"
    Login_message: str = "Logged in succesfully"
    incorrect_password_error: str = "Incorrect password, please try again!"
    verification_error: str = "Please verify your account first"

    if request.method == "POST":
        sleep(2)

        login_user_credentials: dict = request.json
        user_existance = User.query.filter_by(
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

        access_token = create_access_token(
            identity=user_existance)

        user_token = Tokens(
            data=access_token,
            user_id=user_existance.id
        )

        db.session.add(user_token)
        db.session.commit()

        return jsonify({"success": Login_message, "remembered": access_token})

    return jsonify({})


@auth.route("/signup", methods=["POST"])
def signup() -> dict:
    database_insertion_error: str = "Sorry, something went wrong. Please try again."
    success_message: str = "Account created succesfully. A verification link has been sent to your email"
    duplicate_error_message: str = "Email already exist!"
    user_verification_message: str = "There's an error while sending the email, please try again"

    if request.method == "POST":
        sleep(2)
        signup_user_credentials: dict = request.json
        user_existance: bool = User.query.filter_by(
            email=signup_user_credentials["email"]).first()
        validated: bool | dict = Validated(signup_user_credentials).valid()

        if isinstance(validated, dict):
            return jsonify(validated)

        if user_existance:
            return jsonify({"error": duplicate_error_message})

        user_verification = Smt(server=server, mail=mail, access="auth.confirm_email",
                                data=signup_user_credentials["email"]).send()

        if not user_verification:
            return jsonify({"error": user_verification_message})

        try:
            users = User(
                user_name=signup_user_credentials["name"],
                email=signup_user_credentials["email"],
                confirmed=False,
                password=generate_password_hash(
                    signup_user_credentials["password"], method="pbkdf2:sha256")
            )

            db.session.add(users)
            db.session.commit()

            return jsonify({"success": success_message})
        except Exception:
            return jsonify({"error": database_insertion_error})

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
    try:
        confirm_serializer = URLSafeTimedSerializer(
            server.config['SECRET_KEY'])
        email = confirm_serializer.loads(
            token, salt=server.config['SECURITY_PASSWORD_SALT'], max_age=3600)
    except Exception:
        return render_template("confirmation_template.html",
                               content={
                                   "content": "The confirmation link is expired, or invalid token! ❌",
                                   "color": "crimson"
                               })

    if not isinstance(email, str):
        return redirect(f"http://127.0.0.1:5000/index/{token}")

    user = User.query.filter_by(email=email).first()

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
