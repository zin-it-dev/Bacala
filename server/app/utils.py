import hashlib, json, os.path as op

from flask import request, session
from flask_mail import Message
from config import Config


def decode_avatar(email=None, size=128, default="identicon", rating="g"):
    digest = hashlib.md5(email.lower().encode("utf-8")).hexdigest()
    return f"https://www.gravatar.com/avatar/{digest}?s={size}&d={default}&r={rating}"


def get_locale():
    if request.args.get("lang"):
        session["lang"] = request.args.get("lang")
    return session.get("lang", "en")


def load_json(file_name):
    path = op.join(op.abspath(op.dirname(__file__)), 'data', f'{file_name}.json')
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)
    
    
def send_email(to_email, subject):
    from .extensions import mail
    msg = Message(
        subject=subject,
        sender=Config.MAIL_DEFAULT_SENDER,
        recipients=[to_email],
        body="Hello"
    )
    mail.send(msg)