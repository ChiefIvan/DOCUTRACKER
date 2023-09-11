from flask import url_for, render_template
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message


class Smt:
    def __init__(self, server, mail, email: str):
        self.server = server
        self.mail = mail
        self.email = email

    def send(self) -> bool:
        try:
            confirm_serializer = URLSafeTimedSerializer(
                self.server.config["SECRET_KEY"])
            confirm_url = url_for("auth.confirm_email", token=confirm_serializer.dumps(
                self.email, salt=self.server.config["SECURITY_PASSWORD_SALT"]), _external=True)
            template = render_template(
                "email_content.html", confirm_url=confirm_url)
            msg = Message(
                recipients=[self.email], subject="Account Verification", html=template)
            self.mail.send(msg)
        except Exception:
            return False

        return True
