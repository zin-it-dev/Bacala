from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flask_debugtoolbar import DebugToolbarExtension

from .apis import Api

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
cors = CORS(resources={r'/*': {'origins': '*'}})
api = Api(version='1.0', title='Bacala APIs 📚', description='', doc='/')
toolbar = DebugToolbarExtension()