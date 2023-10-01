from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User

views = Blueprint("views", __name__)


@views.route("/index", methods=["GET"])
@jwt_required()
def index() -> dict:
    if request.method == "GET":
        current_user = get_jwt_identity()
        user: User = User.query.filter_by(id=current_user).first()
        return jsonify({"id": user.id, "email": user.email,  "user_name": user.user_name})
