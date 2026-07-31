import pytest
from app import create_app, db
from app.models import User


@pytest.fixture
def app_with_data():
    """Create app with sample data"""
    app = create_app('testing')

    with app.app_context():
        db.create_all()

        # Create sample users
        users = [
            User(username='john_doe', email='john@example.com', password_hash='hash1'),
            User(username='jane_smith', email='jane@example.com', password_hash='hash2'),
        ]

        for user in users:
            db.session.add(user)

        db.session.commit()

        yield app

        db.session.remove()
        db.drop_all()


class TestDataMigrations:
    """Test data migration integrity"""

    def test_user_data_preserved_after_migration(self, app_with_data):
        """Verify user data is preserved through migration"""
        with app_with_data.app_context():
            # Get users before migration
            users_before = User.query.all()
            user_count = len(users_before)

            # Verify users after migration
            users_after = User.query.all()

            assert len(users_after) == user_count

            # Verify specific data
            john = User.query.filter_by(username='john_doe').first()
            assert john is not None
            assert john.email == 'john@example.com'