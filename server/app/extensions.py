from flask_migrate import Migrate
from flask_restx import Api as Api_
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_login import LoginManager


class Api(Api_):
    def add_namespace(self, ns, path=None):
        """
        This method registers resources from namespace for current instance of api.
        You can use argument path for definition custom prefix url for namespace.

        :param Namespace ns: the namespace
        :param path: registration prefix of namespace
        """
        if ns not in self.namespaces:
            self.namespaces.append(ns)

            self.sort_namespace()

            if self not in ns.apis:
                ns.apis.append(self)
            if path is not None:
                self.ns_paths[ns] = path

        for r in ns.resources:
            urls = self.ns_urls(ns, r.urls)
            self.register_resource(ns, r.resource, *urls, **r.kwargs)

        for name, definition in ns.models.items():
            self.models[name] = definition
        if not self.blueprint and self.app is not None:
            self._configure_namespace_logger(self.app, ns)

    def sort_namespace(self):
        """Sort swagger UI sections based on namespace name."""
        self.namespaces = sorted(self.namespaces, key=lambda ns: ns.name)


api = Api(
    title="BridgeTalent",
    version="1.0",
    description="Smart job matching platform 💰",
    doc="/",
    authorizations={"apikey": {"type": "apiKey", "in": "header", "name": "token"}},
)
db = SQLAlchemy()
migrate = Migrate()
cors = CORS(resources={r"/*": {"origins": "*"}})
login_manager = LoginManager()

login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
login_manager.login_message_category = 'info'


def init_apps(app):
    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)