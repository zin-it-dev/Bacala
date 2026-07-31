# errors.py
from flask_restful import Api

class APIError(Exception):
    """Base class for API errors."""
    def __init__(self, message, status_code=400, payload=None):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.payload = payload

class NotFoundError(APIError):
    """Resource not found."""
    def __init__(self, resource_type, resource_id):
        super().__init__(
            message=f"{resource_type} with id {resource_id} not found",
            status_code=404
        )

class ValidationError(APIError):
    """Input validation failed."""
    def __init__(self, errors):
        super().__init__(
            message="Validation failed",
            status_code=400,
            payload={"errors": errors}
        )

class AuthenticationError(APIError):
    """Authentication required or failed."""
    def __init__(self, message="Authentication required"):
        super().__init__(message=message, status_code=401)

class AuthorizationError(APIError):
    """User lacks permission."""
    def __init__(self, message="Permission denied"):
        super().__init__(message=message, status_code=403)