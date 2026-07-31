# app/services/user_service.py

from typing import Optional
from app import db
from models import User


class UserService:
    """
    Service class for user-related business logic.

    This layer sits between views and models, containing
    all business rules and complex operations.
    """

    def authenticate(self, email: str, password: str) -> Optional[User]:
        """
        Authenticate a user by email and password.

        Args:
            email: User's email address
            password: Plain text password to verify

        Returns:
            User object if authentication succeeds, None otherwise
        """
        user = db.session.execute(
            db.select(User).filter_by(email=email)
        ).scalar_one_or_none()

        # Check if user exists and password is correct
        if user and user.check_password(password):
            # Additional checks can go here
            # For example: is the account active? Is email verified?
            if user.is_active:
                return user

        return None

    def create_user(self, email: str, username: str, password: str,
                    is_admin: bool = False) -> User:
        """
        Create a new user account.

        Args:
            email: Unique email address
            username: Display name
            password: Plain text password (will be hashed)
            is_admin: Whether user has admin privileges

        Returns:
            Newly created User object
        """
        user = User(
            email=email,
            username=username,
            is_admin=is_admin
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return user

    def get_by_email(self, email: str) -> Optional[User]:
        """Find a user by email address."""
        return db.session.execute(
            db.select(User).filter_by(email=email)
        ).scalar_one_or_none()

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Find a user by ID."""
        return db.session.get(User, user_id)

    def update_user(self, user_id: int, data: dict) -> Optional[User]:
        """
        Update user profile information.

        Args:
            user_id: ID of user to update
            data: Dictionary of fields to update

        Returns:
            Updated User object or None if not found
        """
        user = self.get_by_id(user_id)
        if not user:
            return None

        # Only update allowed fields
        allowed_fields = ['username', 'email']
        for field in allowed_fields:
            if field in data:
                setattr(user, field, data[field])

        # Handle password separately
        if 'password' in data:
            user.set_password(data['password'])

        db.session.commit()
        return user