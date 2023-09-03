from flask import Flask
from config import Config
from .routes.actor_bp import actor_bp

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(actor_bp)

    return app