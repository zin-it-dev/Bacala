from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension
from flask_babel import Babel
from flask_mail import Mail
from flask_caching import Cache

from config import Config
from .apis import Api
from .utils import get_locale

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