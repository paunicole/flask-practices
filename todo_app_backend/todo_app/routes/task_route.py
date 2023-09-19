from flask import Blueprint
from ..controllers.task_controller import TaskController

bp_tasks = Blueprint('tasks', __name__)

bp_tasks.route('/', methods=['GET'])(TaskController.get)
bp_tasks.route('/<int:task_id>', methods=['GET'])(TaskController.get_by_id)
bp_tasks.route('/', methods=['POST'])(TaskController.create)
bp_tasks.route('/<int:task_id>', methods=['PUT'])(TaskController.update)
bp_tasks.route('/<int:task_id>', methods=['DELETE'])(TaskController.delete)