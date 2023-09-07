import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, to_email: str, subject: str, body: str, password: str, from_email: str) -> None:
        self.to_email = to_email
        self.subject = subject
        self.body = body
        self.password = password
        self.from_email = from_email
        
    def send_email(self) -> bool:
        self.host: str = 'smtp-mail.outlook.com'
        self.port: int = 587

        context = ssl.create_default_context()

        with smtplib.SMTP(self.host, self.port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self.from_email, self.password)

            # Prepare the email
            message = MIMEMultipart()
            message['From'] = self.from_email
            message['To'] = self.to_email
            message['Subject'] = self.subject
            message.attach(MIMEText(self.body, 'plain'))

            # Send the email
            server.sendmail(from_addr=self.from_email, to_addrs=self.to_email, msg=message.as_string())

            print('Sent!')
            return True