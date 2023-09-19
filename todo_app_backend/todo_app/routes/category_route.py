from flask import Blueprint
from ..controllers.category_controller import CategoryController

bp_categories = Blueprint('categories', __name__)

bp_categories.route('/', methods=['GET'])(CategoryController.get)
bp_categories.route('/<int:category_id>', methods=['GET'])(CategoryController.get_by_id)
bp_categories.route('/', methods=['POST'])(CategoryController.create)
bp_categories.route('/<int:category_id>', methods=['PUT'])(CategoryController.update)
bp_categories.route('/<int:category_id>', methods=['DELETE'])(CategoryController.delete)