from ..models.actor_model import Actor
from flask import request

class ActorController:
    
    @classmethod
    def create_actor(self):
        actor = Actor(
            first_name = request.args.get('first_name', ''),
            last_name = request.args.get('last_name', ''),\
            last_update = request.args.get('last_update', '')
        )
        Actor.create_actor(actor)
        return {'message': 'Actor creado con exito'}, 200
    
    @classmethod
    def get_actor(self, actor_id):
        actor_instance = Actor.get_actor(actor_id)

        if actor_instance:
            return {
                "id": actor_instance.actor_id,
                "nombre": actor_instance.first_name,
                "apellido": actor_instance.last_name,
                "ultima_actualizacion": actor_instance.last_update,
            }, 200
    
    @classmethod
    def update_actor(self, actor):
        #Implementación del método
        pass
    
    @classmethod
    def delete_actor(self, actor):
        #Implementación del método
        pass
    
    @classmethod
    def delete_actors(self):
        #Implementación del método
        pass