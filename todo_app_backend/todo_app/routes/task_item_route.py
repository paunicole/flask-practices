from flask import Blueprint
from ..controllers.task_item_controller import TaskItemController

bp_task_items = Blueprint('task_items', __name__)

bp_task_items.route('/', methods=['GET'])(TaskItemController.get)
bp_task_items.route('/<int:ti_id>', methods=['GET'])(TaskItemController.get_by_id)
bp_task_items.route('/', methods=['POST'])(TaskItemController.create)
bp_task_items.route('/<int:ti_id>', methods=['PUT'])(TaskItemController.update)
bp_task_items.route('/<int:ti_id>', methods=['DELETE'])(TaskItemController.delete)