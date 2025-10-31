from flask import Flask

from config import settings
from .extensions import initialize_firebase, initialize_extensions, login_manager, api


def create_app(config_name = 'local'):
    """Application-factory pattern"""

    app = Flask(__name__)
    app.config.from_object(settings[config_name])
    
    # Firebase
    initialize_firebase(app)
    
    initialize_extensions(app)
    
    from .repositories import UserRepository
        
    @login_manager.user_loader
    def load_user(user_id):
        return UserRepository().get_by_id(user_id)
    
    # APIs
    register_views(app)
    register_namespaces(api)
    
    # CLI
    register_command(app)
    
    return app


def register_views(app):
    from .controllers import login, barchart_json
    
    app.add_url_rule('/auth', view_func=login, methods=['POST'])
    app.add_url_rule('/stats/amount', view_func=barchart_json, methods=['GET'])
    
def register_namespaces(api):
    from .resources import category_ns, book_ns
    
    api.add_namespace(category_ns)
    api.add_namespace(book_ns)
    
    
def register_command(app):
    from .commands import create_superuser, seed_db
    
    app.cli.add_command(create_superuser)
    app.cli.add_command(seed_db)