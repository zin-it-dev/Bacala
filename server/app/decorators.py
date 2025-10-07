from flask import redirect, url_for, request, abort
from flask_login import current_user
from functools import wraps
from firebase_admin import auth
    
from .models import Role

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated and current_user.role.__eq__(Role.ADMIN):
            return redirect(url_for("admin"))

        return f(*args, **kwargs)

    return decorated


def firebase_auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            abort(401, description="Authorization token missing")

        try:
            if token.startswith('Bearer '):
                id_token = token[7:]
            
            decoded_token = auth.verify_id_token(id_token)
            request.user_id = decoded_token['uid']
        except Exception as e:
            abort(401, description=f"Invalid or expired token: {e}")
        
        return f(*args, **kwargs)
    
    return decorated