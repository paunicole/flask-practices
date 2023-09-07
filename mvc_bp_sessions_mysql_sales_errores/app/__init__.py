from flask import Flask
from config import Config

from .routes.staff_bp import staff_bp
from .routes.error_handlers import errors

from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    app.config.from_object(
        Config
    )

    DatabaseConnection.set_config(app.config)

    app.register_blueprint(staff_bp, url_prefix = '/staffs')
    
    app.register_blueprint(errors, url_prefix = '/errors')

    return app