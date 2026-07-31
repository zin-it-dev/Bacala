import pytest
from flask import current_app
from app import create_app, db
from app.models import User


@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            assert current_app.config["ENV"] == "production"
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()


@pytest.fixture
def app():
    """Create test application"""
    app = create_app('testing')

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def runner(app):
    """Create CLI runner."""
    return app.test_cli_runner()


@pytest.fixture
def auth_client(app, client):
    """
    Create authenticated test client.
    Creates a test user and logs them in.
    """
    with app.app_context():
        # Create test user
        user = User(
            email='test@example.com',
            username='testuser'
        )
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()

        # Log in the user
        client.post('/auth/login', data={
            'email': 'test@example.com',
            'password': 'password123'
        })

    return client