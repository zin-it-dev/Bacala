import firebase_admin, os, json

from firebase_admin import credentials
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_babel import Babel
from flask_mail import Mail
from flask_caching import Cache

from .apis import Api
from .utils import get_locale
from config import firebase_dir

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
cors = CORS(resources={r'/*': {'origins': '*'}})
api = Api(
    version='1.0', 
    title='Bacala APIs 📚', 
    description=(
        "📚 Read and share books 📖👐\n"
        "📍 A platform to explore books, manage a personal library, and share reviews with the community 🐧"
    ), 
    doc='/',
    contact="zin.it.dev@gmail.com",
    contact_email="zin.it.dev@gmail.com",
    license="MIT License",
    terms_url="https://www.google.com/policies/terms/"
)
toolbar = DebugToolbarExtension()
babel = Babel(locale_selector=get_locale)
mail = Mail()
cache = Cache()

def initialize_firebase(app):
    if firebase_admin._apps or app.testing:
        return
    
    if app.debug and os.path.exists(firebase_dir):
        cred = credentials.Certificate(firebase_dir)
        firebase_admin.initialize_app(cred)
        

def initialize_extensions(app):
    from .admin import manager
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cors.init_app(app)
    babel.init_app(app)
    manager.init_app(app)
    api.init_app(app)
    mail.init_app(app)
    cache.init_app(app)
    
    if app.debug:
        toolbar.init_app(app)