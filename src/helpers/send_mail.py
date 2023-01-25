from os import environ
from flask_mail import Message
from src.extension import mail
from datetime import timedelta
from flask_jwt_extended import create_access_token
from flask import render_template
from src.settings import SITE_NAME,MAIL_USERNAME


def send_email(user, subject, template):
    """ Send email """
    print(SITE_NAME)
    token = create_access_token(identity=str(user.get("id")), expires_delta=timedelta(days=5))
    msg = Message(subject,
                  sender=(SITE_NAME,MAIL_USERNAME), recipients=[user['email']])
    msg.html = render_template(template, user=user, token=token)

    mail.send(msg)
