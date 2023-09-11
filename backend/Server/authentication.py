from flask import Blueprint, jsonify, request, render_template
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer
from time import sleep
from . import db, mail, server
from .models import User
from .static.predef_function.Validation import Validated
from .static.predef_function.smt import Smt

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login() -> dict:
    sleep(2)
    user_existance_error: str = "Account Doesn't Exist"
    Login_message: str = "Logged in succesfully"
    incorrect_password_error: str = "Incorrect password, please try again!"
    verification_error: str = "Please verify your account first"

    if request.method == "POST":
        login_user_credentials: dict = request.json
        user_existance: bool = User.query.filter_by(
            email=login_user_credentials["email"]).first()

        if not user_existance:
            return jsonify({"error": user_existance_error})

        if not user_existance.confirmed:
            return jsonify({"error": verification_error})

        if not check_password_hash(user_existance.password, login_user_credentials["password"]):
            return jsonify({"error": incorrect_password_error})

        login_user(user_existance, remember=True)
        return jsonify({"success": Login_message})

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

        user_verification = Smt(server=server, mail=mail,
                                email=signup_user_credentials["email"]).send()

        if not user_verification:
            return jsonify({"error": user_verification_message})

        try:
            users = User(
                user_name=signup_user_credentials["name"],
                email=signup_user_credentials["email"],
                confirmed=False,
                password=generate_password_hash(
                    signup_user_credentials["password"], method="scrypt")
            )

            db.session.add(users)
            db.session.commit()

            return jsonify({"success": success_message})
        except Exception:
            return jsonify({"error": database_insertion_error})

    return jsonify({})


@auth.route("/logout", methods=["GET"])
def logout():
    return jsonify({"success": "Logged out succesfully"})


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


@auth.route('/<token>', methods=['GET'])
def confirm_email(token):
    try:
        confirm_serializer = URLSafeTimedSerializer(
            server.config['SECRET_KEY'])
        email = confirm_serializer.loads(
            token, salt=server.config['SECURITY_PASSWORD_SALT'], max_age=3600)
    except Exception:
        return render_template("confirmation_template.html", content="The confirmation link is expired!")

    user = User.query.filter_by(email=email).first()

    if user.confirmed:
        return render_template("confirmation_template.html", content="Email already confirmed")

    else:
        user.confirmed = True
        db.session.add(user)
        db.session.commit()
        return render_template("confirmation_template.html", content="Email confirmed")
