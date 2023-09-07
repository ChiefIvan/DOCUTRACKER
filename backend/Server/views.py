from flask import Blueprint, jsonify
from flask_login import current_user


views = Blueprint("views", __name__)


@views.route("/index", methods=["GET", "POST"])
# @login_required
def content():
    print(current_user.is_authenticated)  
    return jsonify({})
        
