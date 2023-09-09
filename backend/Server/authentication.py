from flask import Blueprint, jsonify, request
from . import db
from .models import User
from flask_login import login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .static.Validation import Validated
from .static.smt import Email
from .static.system_credetials import EMAIL, PASSWORD
from threading import Timer
import json

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login() -> dict:
    user_existance_error: str = "Account Doesn't Exist"
    Login_message: str = "Logged in succesfully"
    incorrect_password_error: str = "Incorrect password, please try again!"

    if request.method == "POST":
        login_user_credentials: dict = request.json
        additional_credentials: dict = {"name": None, "confirm_password": None}
        login_user_credentials |= additional_credentials
        user_existance: bool = User.query.filter_by(
            email=login_user_credentials["email"]).first()
        validated: bool | dict = Validated(login_user_credentials).valid()

        if isinstance(validated, dict):
            return jsonify(validated)

        if not user_existance:
            return jsonify({"error": user_existance_error})

        if not check_password_hash(user_existance.password, login_user_credentials["password"]):
            return jsonify({"error": incorrect_password_error})

        login_user(user_existance, remember=True)
        return jsonify({"success": Login_message})

    return jsonify({})


@auth.route("/signup", methods=["POST"])
def signup() -> dict:
    database_insertion_error: str = "Sorry, something went wrong. Please try again."
    success_message: str = "Account created succesfully, a verification link has been sent to your email"
    duplicate_error_message: str = "Account already exist!"

    if request.method == "POST":
        signup_user_credentials: dict = request.json
        user_existance: bool = User.query.filter_by(
            email=signup_user_credentials["email"]).first()
        validated: bool | dict = Validated(signup_user_credentials).valid()

        if isinstance(validated, dict):
            return jsonify(validated)

        if user_existance:
            return jsonify({"error": duplicate_error_message})

        try:
            users = User(
                user_name=signup_user_credentials["name"],
                email=signup_user_credentials["email"],
                password=generate_password_hash(
                    signup_user_credentials["password"], method="scrypt")
            )

            db.session.add(users)
            db.session.commit()
            login_user(users, remember=True)
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
    reset_user_credentials |= {"name": None,
                               "password": None, "confirm_password": None}
    validated: bool | dict = Validated(reset_user_credentials).valid()
    user_existance: bool = User.query.filter_by(
        email=reset_user_credentials["email"]).first()
    if isinstance(validated, dict):
        return jsonify(validated)

    if not user_existance:
        return jsonify({"error": user_existance_error})

    with open("C:\\Users\\User\\Documents\\My Project\\DOCUTRACKER\\backend\\Server\\static\\data.json", "r+") as file:
        data = json.load(file)
        if data["password_change"] == 0:
            return jsonify({"error": change_duration_message})

        password_changes = Email(to_email=user_existance.email, subject='hello',
                                 body='this is a message', password=PASSWORD, from_email=EMAIL).send_email()
        if password_changes:
            data["password_change"] = 0
            file.seek(0)
            json.dump(data, file)
            print(data["password_change"])

    # print(changes)

    # def time():
    #     changes = changes + 1
    # Timer(7 * 86, 400, time).start()

    return jsonify({})
