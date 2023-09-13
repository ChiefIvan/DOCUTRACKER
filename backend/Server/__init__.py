from flask import Flask
from os import path
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from .static.predef_function.system_credentials import EMAIL, PASSWORD, SECRET_KEY, SALT, CORS_LINK
from gevent.pywsgi import WSGIServer
# from geventwebsocket.handler import WebSocketHandler

server = Flask(__name__)
db = SQLAlchemy()
mail = Mail()


class Flaskserver:
    CORS(server, resources={r"/*": {"origins": CORS_LINK}})
    DB_NAME = "database.db"

    def __init__(self):
        self.server = server
        self.http_server = WSGIServer(('localhost', 5000), self.server)
        # handler_class=WebSocketHandler
        self.server.config["SECRET_KEY"] = SECRET_KEY
        self.server.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{self.DB_NAME}"
        self.server.config["MAIL_SERVER"] = 'smtp-mail.outlook.com'
        self.server.config["MAIL_PORT"] = 587
        self.server.config["MAIL_USE_TLS"] = True
        self.server.config["MAIL_USE_SSL"] = False
        self.server.config["SECURITY_PASSWORD_SALT"] = SALT
        self.server.config["MAIL_USERNAME"] = EMAIL
        self.server.config["MAIL_PASSWORD"] = PASSWORD
        self.server.config["MAIL_DEFAULT_SENDER"] = EMAIL

        db.init_app(self.server)
        mail.init_app(self.server)

        from .models import User
        from .authentication import auth
        from .views import views

        self.server.register_blueprint(auth, url_prefix="/")
        self.server.register_blueprint(views, url_prefix="/")

        with self.server.app_context():
            if not path.exists(self.DB_NAME):
                db.create_all()

    def server_run(self):
        return self.http_server
        # return self.server
