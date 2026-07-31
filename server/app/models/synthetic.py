from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, Text, DateTime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db, login_manager


class User(UserMixin, db.Model):
    """User model for authentication."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    first_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    bio = Column(Text, nullable=True)
    avatar = Column(String(255), default=None)

    dated_created = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    dated_updated = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    def set_password(self, password):
        """Hash and store password."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Verify password against hash."""
        return check_password_hash(self.password, password)

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return f"@{self.username}"

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'date_created': self.date_created.isoformat()
        }

    def __str__(self):
        return f"@{self.username}"


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID for Flask-Login."""
    return User.query.get(int(user_id))