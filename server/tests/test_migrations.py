import pytest
from alembic.config import Config
from alembic import command
from app import db


class TestMigrations:
    """Test migration up and down operations"""

    def test_upgrade_to_head(self, app):
        """Test that all migrations can be applied"""
        with app.app_context():
            alembic_cfg = Config('migrations/alembic.ini')
            alembic_cfg.set_main_option('script_location', 'migrations')

            # Start from empty database
            command.downgrade(alembic_cfg, 'base')

            # Apply all migrations
            command.upgrade(alembic_cfg, 'head')

            # Verify tables exist
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()

            assert 'users' in tables
            assert 'posts' in tables
            assert 'alembic_version' in tables

    def test_downgrade_to_base(self, app):
        """Test that all migrations can be reversed"""
        with app.app_context():
            alembic_cfg = Config('migrations/alembic.ini')
            alembic_cfg.set_main_option('script_location', 'migrations')

            # Start from head
            command.upgrade(alembic_cfg, 'head')

            # Downgrade all migrations
            command.downgrade(alembic_cfg, 'base')

            # Verify tables are removed (except alembic_version)
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()

            assert 'users' not in tables
            assert 'posts' not in tables

    def test_upgrade_downgrade_cycle(self, app):
        """Test upgrade/downgrade cycle for each migration"""
        with app.app_context():
            alembic_cfg = Config('migrations/alembic.ini')
            alembic_cfg.set_main_option('script_location', 'migrations')

            # Start from base
            command.downgrade(alembic_cfg, 'base')

            # Get all revisions
            from alembic.script import ScriptDirectory
            script = ScriptDirectory.from_config(alembic_cfg)
            revisions = list(script.walk_revisions('head', 'base'))

            # Test each migration individually
            for rev in reversed(revisions):
                # Upgrade to this revision
                command.upgrade(alembic_cfg, rev.revision)

                # Downgrade from this revision
                command.downgrade(alembic_cfg, '-1')

                # Upgrade again
                command.upgrade(alembic_cfg, rev.revision)