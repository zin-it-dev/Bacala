from flask import Flask
from app.config import config_by_name, CONFIG_TYPE
from app.extensions import init_apps, db
from app.apis import api


def create_app(config_type=CONFIG_TYPE):
    """
    Application factory function.

    Args:
        config_type: Configuration to use (development, production, testing)

    Returns:
        Configured Flask application instance
    """

    app = Flask(__name__)
    app.config.from_object(config_by_name[config_type])
    config_by_name[config_type].init_app(app)
    
    # Initialize extensions
    init_apps(app)
    api.init_app(app)

    from app import models  # noqa: F401
    
    # Register error handlers
    from app.utils.errors import register_error_handlers
    register_error_handlers(app)

    return app