from flask import Blueprint
from ..controllers.actor_controller import ActorController

actor_bp = Blueprint('actor_bp',__name__)

actor_bp.route('/actors/<int:actor_id>', methods = ['GET'])(ActorController.get_actor)
actor_bp.route('/actors/<int:actor_id>', methods = ['PUT'])(ActorController.update_actor)
actor_bp.route('/actors', methods = ['DELETE'])(ActorController.delete_actors)
actor_bp.route('/actors/<int:actor_id>', methods = ['DELETE'])(ActorController.delete_actor)