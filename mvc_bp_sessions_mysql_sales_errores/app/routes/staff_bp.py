from flask import Blueprint
from ..controllers.staff_controller import StaffController

staff_bp = Blueprint('staff_bp',__name__)

staff_bp.route('/', methods = ['POST'])(StaffController.create_staff)
staff_bp.route('/<int:staff_id>', methods = ['PUT'])(StaffController.update_staff)
staff_bp.route('/', methods = ['GET'])(StaffController.get_staffs)
staff_bp.route('/<int:staff_id>', methods = ['GET'])(StaffController.get_staff)
staff_bp.route('/<int:staff_id>', methods = ['DELETE'])(StaffController.delete_staff)