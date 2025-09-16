from flask import Flask

from .extensions import db, migrate, login_manager, api, cors, toolbar, babel, mail, cache
from .admin import manager
from config import settings

def create_app(config_name = 'local'):
    """Application-factory pattern"""
    app = Flask(__name__)
    app.config.from_object(settings[config_name])
    
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


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cors.init_app(app)
    manager.init_app(app)
    api.init_app(app)
    babel.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    
    if app.debug:
        toolbar.init_app(app)
    
    
def register_views(app):
    from .controllers import login, linechart_json
    
    app.add_url_rule('/auth', view_func=login, methods=['POST'])
    app.add_url_rule('/chart/stats', view_func=linechart_json, methods=['GET'])
    
def register_namespaces(api):
    from .resources import category_ns, book_ns
    
    api.add_namespace(category_ns)
    api.add_namespace(book_ns)
    
    
def register_command(app):
    from .commands import create_superuser, seed_db
    app.cli.add_command(create_superuser)
    app.cli.add_command(seed_db)