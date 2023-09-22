from flask import url_for, render_template
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
# from threading import Thread


class Smt:
    def __init__(self, server, mail, access: str = "", data: str = ""):
        self.server = server
        self.mail = mail
        self.data = data
        self.access = access

    def authentication(self) -> str:
        confirm_serializer = URLSafeTimedSerializer(
            self.server.config["SECRET_KEY"])
        confirm_url = url_for(self.access, token=confirm_serializer.dumps(
            self.data, salt=self.server.config["SECURITY_PASSWORD_SALT"]), _external=True)
        return confirm_url

    def send(self) -> None:
        user_verification_message: str = "There's an error while sending the email, please try again"

        try:
            confirm_url = self.authentication()
            template = render_template(
                "email_content.html", confirm_url=confirm_url)
            msg = Message(
                recipients=[self.data], subject="Verify your Email", html=template)
            self.mail.send(msg)
        except Exception:
            print(user_verification_message)
