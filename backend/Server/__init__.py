from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_jwt_extended import JWTManager

from sqlalchemy import inspect
from uuid import uuid4
from datetime import timedelta
# from gevent.pywsgi import WSGIServer

from .static.predef_function.server_credentials import EMAIL, PASSWORD, CORS_LINK


server: Flask = Flask(__name__)
db: SQLAlchemy = SQLAlchemy()
mail: Mail = Mail()
jwt: JWTManager = JWTManager()


class Flaskserver:
    CORS(
        server,
        resources={r"/*": {"origins": CORS_LINK}}
    )

    def __init__(self):

        self.server = server
        # self.http_server = WSGIServer(('localhost', 5000), self.server)

        self.server.config["SECRET_KEY"] = str(uuid4())
        self.server.config["JWT_SECRET_KEY"] = str(uuid4())
        self.server.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
        self.server.config["SECURITY_PASSWORD_SALT"] = str(uuid4())
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

        from .models import User, Captcha, Revoked
        from .authentication import auth
        from .views import views

        self.server.register_blueprint(auth, url_prefix="/")
        self.server.register_blueprint(views, url_prefix="/")

        try:
            with self.server.app_context():
                with db.engine.connect() as connection:
                    inspector = inspect(connection)
                    if "user" and "captcha" and "revoked" not in inspector.get_table_names():
                        db.create_all()

        except Exception:
            print("Please enable you database connection!")

        @jwt.user_identity_loader
        def user_loader(user):
            return user.id

        @jwt.user_lookup_loader
        def user_lookup_callback(_jwt_header, jwt_data):
            identity = jwt_data["sub"]
            return User.query.get(int(identity))

    def server_run(self):
        # return self.http_server
        return self.server
