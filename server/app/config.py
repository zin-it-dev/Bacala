import os, secrets
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SECRET_FILE = os.path.normpath(os.path.join(BASE_DIR, "deploy", "SECRET"))

CONFIG_TYPE = os.environ.get("CONFIG_TYPE")


class Config:
    """
    Base configuration class.
    Contains settings common to all environments.
    """
    
    try:
        with open("/path/to/secret/file", mode="r", encoding="utf-8") as f:
            SECRET_KEY = f.read().strip()
    except FileNotFoundError, PermissionError:
        try:
            secret_dir = os.path.dirname(SECRET_FILE)
            os.makedirs(secret_dir, exist_ok=True)

            with open(SECRET_FILE, "w") as f:
                f.write(secrets.token_hex(24))

            if os.name == "posix":
                os.chmod(SECRET_FILE, 0o600)
        except OSError:
            raise Exception("Cannot open file `%s` for writing." % SECRET_FILE)

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024 
    
    REMEMBER_COOKIE_DURATION = timedelta(days=14)
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    PAGE_SIZE = 20
    
    @staticmethod
    def init_app(app):
        """Perform any initialization needed for all environments."""
        pass
    

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True
    
    @staticmethod
    def init_app(app):
        """Production-specific initialization."""
        if not app.config.get('SECRET_KEY'):
            raise RuntimeError('SECRET_KEY must be set in production.')
        if not app.config.get('SQLALCHEMY_DATABASE_URI'):
            raise RuntimeError('DATABASE_URL must be set in production.')

        import logging
        from logging import StreamHandler
        handler = StreamHandler()
        handler.setLevel(logging.WARNING)
        app.logger.addHandler(handler)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 10,
        'pool_recycle': 3600,
        'max_overflow': 10,
        'pool_timeout': 30,
        "connect_args": {
            "sslmode": "require"
        },
        'pool_pre_ping': True
    }
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    TESTING = True
    WTF_CSRF_ENABLED = False 


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}
