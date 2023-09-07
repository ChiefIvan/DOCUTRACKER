from flask import Flask
from os import path
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta
# from gevent.pywsgi import WSGIServer
# from geventwebsocket.handler import WebSocketHandler

server = Flask(__name__)
db = SQLAlchemy()


class Flaskserver:
    CORS(server, resources={r"/*": {"origins": "http://localhost:5173"}})
    DB_NAME = "database.db"
    
    def __init__(self):
        self.server = server
        # self.http_server = WSGIServer(('localhost', 5000), self.server, handler_class=WebSocketHandler)
        self.server.config["SECRET_KEY"] = "JustSomeRandomKey0111"
        self.server.config["SESSION_TYPE"] = "filesystem"
        self.server.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=7)  # Example duration
        self.server.config["SESSION_COOKIE_HTTPONLY"] = True
        self.server.config["SESSION_USE_SIGNER"] = True
        self.server.config["SESSION_KEY_PREFIX"] = "JustSomeRandomKey0111"
        self.server.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{self.DB_NAME}"
        db.init_app(self.server)
        
        from .models import User        
        from .authentication import auth
        from .views import views

        self.server.register_blueprint(auth, url_prefix="/")
        self.server.register_blueprint(views, url_prefix="/")
        
        with self.server.app_context():
            if not path.exists(self.DB_NAME):
                db.create_all()
                
        login_manager = LoginManager()
        login_manager.login_view = "auth.login" # type: ignore
        login_manager.init_app(self.server)    
                
        @login_manager.user_loader
        def load_user(id):
            return User.query.get(id) # type: ignore

    def server_run(self):
        # return self.http_server
        return self.server

