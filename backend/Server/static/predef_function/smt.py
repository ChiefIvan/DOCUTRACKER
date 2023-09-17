from flask import url_for, render_template
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message


class Smt:
    def __init__(self, server, mail, access: str = "", data: str = ""):
        self.server = server
        self.mail = mail
        self.data = data
        self.access = access

    def authentication(self):
        confirm_serializer = URLSafeTimedSerializer(
            self.server.config["SECRET_KEY"])
        confirm_url = url_for(self.access, token=confirm_serializer.dumps(
            self.data, salt=self.server.config["SECURITY_PASSWORD_SALT"]), _external=True)
        return confirm_url

    def send(self) -> bool:
        try:
            confirm_url = self.authentication()
            template = render_template(
                "email_content.html", confirm_url=confirm_url)
            msg = Message(
                recipients=[self.data], subject="Confirm Your Email Address for DOCUTRACKER", html=template)
            self.mail.send(msg)
        except Exception:
            return False

        return True
