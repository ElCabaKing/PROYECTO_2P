from flask_mail import  Message
from src.extensions.mailInit import mail

def send_email(app,email,body,email_subject):
    with app.app_context():
        msg = Message(
        subject=email_subject,
        recipients=[email],
        body=body
        )
        mail.send(msg)