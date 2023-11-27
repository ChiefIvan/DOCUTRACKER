from flask import Blueprint, request, Response, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from datetime import datetime


from .models import User, Revoked, Credentials
from .static.predef_function.user_validation import Sanitizer, RegisterEntryValidator
from .static.predef_function.image_compressor import compress_image
from . import db


views = Blueprint("views", __name__)


@views.route("/index", methods=["GET"])
@jwt_required()
def index() -> dict:
    if request.method == "GET":
        current_user = get_jwt_identity()

        user: User = User.query.filter_by(id=current_user).first()
        user_credentials: Credentials = Credentials.query.filter_by(
            id=user.id).first()

        data = {
            "userImg": user_credentials.user_img if user_credentials else "",
            "email": user.email,
            "user_name": user.user_name,
            "full_ver_val": user.full_verified
        }

        return jsonify(data)

    return jsonify({})


@views.route("/logout", methods=["GET"])
@jwt_required()
def logout() -> dict:
    jti = get_jwt()["jti"]
    now = datetime.now()
    revoked_token = Revoked(jti=jti, revoked_at=now)
    db.session.add(revoked_token)
    db.session.commit()
    return jsonify({})


@views.route("/registration", methods=["POST"])
@jwt_required()
def register():
    insertion_error: str = "Sorry, something went wrong!. Please try again."

    credentials = request.json

    current_user = get_jwt_identity()
    image = credentials["userImg"]
    first_name = credentials["firstName"]
    middle_name = credentials["middleName"]
    last_name = credentials["lastName"]

    entry_validate: RegisterEntryValidator = RegisterEntryValidator(
        image, first_name, middle_name, last_name).validate()

    if isinstance(entry_validate, dict):
        return jsonify(entry_validate)

    sanitize: bool | dict = Sanitizer(
        {"user_image": image, "first_name": first_name,
            "middle_name": middle_name, "last_name": last_name}
    ).validate()

    if isinstance(sanitize, dict):
        return jsonify(sanitize)

    user: User = User.query.filter_by(id=current_user).first()
    user_credentials: Credentials = Credentials.query.filter_by(
        user_id=current_user).first()

    image = compress_image(image, quality=80)

    if not user_credentials:
        try:
            registration: Credentials = Credentials(
                user_img=image,
                firstname=first_name,
                mid_init=middle_name,
                lastname=last_name,
                full_veri_at=datetime.now(),
                user_id=current_user,
            )

            db.session.add(registration)
            user.full_verified = True
            db.session.commit()

        except Exception as e:
            print(e)
            return jsonify({"error": insertion_error})

        return jsonify({})

    user_credentials.user_img = image
    user_credentials.firstname = first_name
    user_credentials.mid_init = middle_name
    user_credentials.lastname = last_name
    user_credentials.full_veri_at = datetime.now()
    user.full_verified = True

    db.session.commit()
    return jsonify({})


@views.route('/user_credentials_updates', methods=["GET"])
@jwt_required()
def event_polling():
    current_user = get_jwt_identity()
    user_credentials: Credentials = Credentials.query.filter_by(
        user_id=current_user).first()
    if user_credentials:
        data = {
            "userImg": user_credentials.user_img,
        }

        return jsonify(data)

    return jsonify({})
