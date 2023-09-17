from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_mail import Mail
from flask_jwt_extended import JWTManager
from datetime import timedelta
from .static.predef_function.server_credentials import (
    EMAIL, PASSWORD, SECRET_KEY, SALT, CORS_LINK, JWT_KEYS)
# from gevent.pywsgi import WSGIServer
# from geventwebsocket.handler import WebSocketHandler

server = Flask(__name__)
db = SQLAlchemy()
mail = Mail()
jwt = JWTManager()


class Flaskserver:
    CORS(server, resources={r"/*": {"origins": CORS_LINK}})

    def __init__(self):

        self.server = server
        # self.http_server = WSGIServer(('localhost', 5000), self.server)
        # handler_class=WebSocketHandler
        self.server.config["SECRET_KEY"] = SECRET_KEY
        self.server.config["JWT_SECRET_KEY"] = JWT_KEYS
        self.server.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
        self.server.config["SECURITY_PASSWORD_SALT"] = SALT
        self.server.config["SQLALCHEMY_DATABASE_URI"] = "mysql://Ban:IvanDawang01112002@localhost/docutracker_db"
        self.server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.server.config["MAIL_SERVER"] = 'smtp-mail.outlook.com'
        self.server.config["MAIL_PORT"] = 587
        self.server.config["MAIL_USE_TLS"] = True
        self.server.config["MAIL_USE_SSL"] = False
        self.server.config["MAIL_USERNAME"] = EMAIL
        self.server.config["MAIL_PASSWORD"] = PASSWORD
        self.server.config["MAIL_DEFAULT_SENDER"] = EMAIL

        db.init_app(self.server)
        mail.init_app(self.server)
        jwt.init_app(self.server)

        from .models import User, Tokenblocklist
        from .authentication import auth
        from .views import views

        self.server.register_blueprint(auth, url_prefix="/")
        self.server.register_blueprint(views, url_prefix="/")

        with self.server.app_context():
            with db.engine.connect() as connection:
                inspector = inspect(connection)
                if "user" and "tokens" and "Tokenblocklist" not in inspector.get_table_names():
                    db.create_all()

        @jwt.user_identity_loader
        def user_loader(user):
            return user.id

        @jwt.user_lookup_loader
        def user_lookup_callback(_jwt_header, jwt_data):
            identity = jwt_data["sub"]
            return User.query.get(int(identity))

        @jwt.token_in_blocklist_loader
        def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
            jti = jwt_payload.get("jti")  # .get method is used instead of square bracket notation
            if jti is None:
                # Handle case here where jti is not included in payload - logic will depend on your app
                raise ValueError("No jti claim found in token payload")

            token = db.session.query(Tokenblocklist.id).filter_by(jti=jti).scalar()
            return token is not None

    def server_run(self):
        # return self.http_server
        return self.server
