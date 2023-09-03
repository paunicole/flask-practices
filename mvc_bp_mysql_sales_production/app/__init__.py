from flask import Flask
from config import Config
from .routes.customer_bp import customer_bp
from .routes.product_bp import product_bp

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(product_bp)

    return app