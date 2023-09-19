from flask import Flask
from config import Config

from .routes.category_route import bp_categories
from .routes.task_route import bp_tasks
from .routes.task_item_route import bp_task_items

from .routes.error_handlers import errors
from .models.exceptions import *

from flask_cors import CORS

def init_app():
    """Crea y configura la aplicación Flask"""
    
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    
    CORS(app, supports_credentials=True)

    app.config.from_object(Config)
    
    app.register_blueprint(bp_categories, url_prefix = '/categories')
    app.register_blueprint(bp_tasks, url_prefix = '/tasks')
    app.register_blueprint(bp_task_items, url_prefix = '/task_items')

    app.register_blueprint(errors)

    return app