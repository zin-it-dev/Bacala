from app.extensions import api
from .resources import user_ns

# Register endpoints
api.add_namespace(user_ns)