from app.extensions import db


def register_error_handlers(app):
    """Register custom error handlers."""

    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Resource not found'}, 404

    @app.errorhandler(500)
    def internal_error(error):
        # Rollback any failed database transactions
        db.session.rollback()
        return {'error': 'Internal server error'}, 500