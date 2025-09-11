import hashlib

from flask import request, session


def decode_avatar(email=None, size=128, default="identicon", rating="g"):
    digest = hashlib.md5(email.lower().encode("utf-8")).hexdigest()
    return f"https://www.gravatar.com/avatar/{digest}?s={size}&d={default}&r={rating}"


def get_locale():
    if request.args.get("lang"):
        session["lang"] = request.args.get("lang")
    return session.get("lang", "en")