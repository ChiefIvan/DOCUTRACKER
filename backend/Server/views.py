from flask import Blueprint, jsonify, redirect
from flask_jwt_extended import jwt_required, get_jwt_identity
from .models import User, Tokens

views = Blueprint("views", __name__)


@views.route("/index", methods=["GET"])
@jwt_required()
def index():
    # try:
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user).first()
    user_token = Tokens.query.filter_by(user_id=user.id).first()
    return jsonify({"id": user.id, "email": user.email,  "user_name": user.user_name, "token": user_token.data})
    # except Exception as e:
    #     return redirect("http://localhost:5173/login")
