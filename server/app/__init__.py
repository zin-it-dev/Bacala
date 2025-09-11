from flask import Flask

from .extensions import db, migrate, login_manager, api, cors, toolbar, babel
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
    
    return app


def initialize_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cors.init_app(app)
    manager.init_app(app)
    api.init_app(app)
    babel.init_app(app)
    
    if app.debug:
        toolbar.init_app(app)
    
    
def register_views(app):
    from .controllers import login
    
    app.add_url_rule('/auth', view_func=login, methods=['POST'])
    
    
def register_namespaces(api):
    from .resources import category_ns
    
    api.add_namespace(category_ns)