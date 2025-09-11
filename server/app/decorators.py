from flask import redirect, url_for
from flask_login import current_user
from functools import wraps

from .models import Role

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated and current_user.role.__eq__(Role.ADMIN):
            return redirect(url_for("admin"))

        return f(*args, **kwargs)

    return decorated