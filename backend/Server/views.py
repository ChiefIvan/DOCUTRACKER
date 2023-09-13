from flask import Blueprint, jsonify, redirect


views = Blueprint("views", __name__)


@views.route("/index", methods=["GET", "POST"])
def content():
    return redirect("http://localhost:5173/home")
