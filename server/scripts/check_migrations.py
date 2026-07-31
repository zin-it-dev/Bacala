"""Pre-deployment migration checks"""
import sys
from flask import Flask
from flask_migrate import Migrate
from alembic.config import Config
from alembic.script import ScriptDirectory
from app import create_app, db


def check_migrations():
    """Verify migration state before deployment"""

    app = create_app('production')

    with app.app_context():
        config = Config('migrations/alembic.ini')
        config.set_main_option('script_location', 'migrations')

        script = ScriptDirectory.from_config(config)

        from alembic.runtime.migration import MigrationContext
        connection = db.engine.connect()
        context = MigrationContext.configure(connection)
        current_rev = context.get_current_revision()

        head_rev = script.get_current_head()

        print(f"Current database revision: {current_rev}")
        print(f"Head revision: {head_rev}")

        if current_rev == head_rev:
            print("Database is up to date.")
            return True

        pending = []
        for rev in script.walk_revisions(head_rev, current_rev):
            if rev.revision != current_rev:
                pending.append(rev)

        print(f"\nPending migrations ({len(pending)}):")
        for rev in reversed(pending):
            print(f"  - {rev.revision}: {rev.doc}")

        return False


if __name__ == '__main__':
    is_current = check_migrations()
    sys.exit(0 if is_current else 1)