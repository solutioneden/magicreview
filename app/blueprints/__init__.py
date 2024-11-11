from .api import api_bp


def register_blueprints(app):
    """
    Registers all Blueprint instances with the Flask application.
    """
    app.register_blueprint(api_bp, url_prefix="/api")
