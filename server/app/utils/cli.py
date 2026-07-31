from app.extensions import db


def register_cli_commands(app):
    """Register custom CLI commands."""

    @app.cli.command()
    def init_db():
        """Initialize the database."""
        db.create_all()
        print('Database initialized.')