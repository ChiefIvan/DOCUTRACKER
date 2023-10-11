from flask import Blueprint, jsonify, request, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from datetime import timezone, datetime

from .models import User, Revoked
from . import db

views = Blueprint("views", __name__)


@views.route("/index", methods=["GET"])
@jwt_required()
def index() -> dict:
    if request.method == "GET":
        current_user = get_jwt_identity()
        user: User = User.query.filter_by(id=current_user).first()
        return jsonify({"email": user.email,  "user_name": user.user_name, "fully_ver_val": user.full_verified})


@views.route("/logout", methods=["GET"])
@jwt_required()
def logout() -> dict:
    jti = get_jwt()["jti"]
    now = datetime.now(timezone.utc)
    revoked_token = Revoked(jti=jti, revoked_at=now)
    db.session.add(revoked_token)
    db.session.commit()
    return jsonify({})
