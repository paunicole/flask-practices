from flask import Flask, request, render_template
from config import Config
from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    
    @app.route('/')
    def bienvenida():
        return 'Pagina de bienvenida'

    @app.route('/actors/<int:actor_id>', methods = ['GET'])
    def get_actor(actor_id):
        query = "SELECT actor_id, first_name, last_name, last_update FROM sakila.actor WHERE actor_id = %s;"
        params = actor_id,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return {
                "id": result[0],
                "nombre": result[1],
                "apellido": result[2],
                "ultima_actualizacion": result[3]
            }, 200
        return {"msg": "No se encontró el actor"}, 404

    @app.route('/actors', methods = ['GET'])
    def get_actors():
        query = "SELECT actor_id, first_name, last_name, last_update FROM sakila.actor;"
        results = DatabaseConnection.fetch_all(query)
        actors = []
        for result in results:
            actors.append({
                "id": result[0],
                "nombre": result[1],
                "apellido": result[2],
                "ultima_actualizacion": result[3]
            })
        return actors, 200

    @app.route('/actors', methods = ['POST'])
    def create_actor():
        query= "INSERT INTO sakila.actor (first_name, last_name, last_update) VALUES (%s,%s,%s);"
        params = request.args.get('first_name', ''), request.args.get('last_name', ''), request.args.get('last_update', '')
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Actor creado con éxito"}, 201

    @app.route('/actors/<int:actor_id>', methods = ['PUT'])
    def update_actor(actor_id):
        query = "UPDATE sakila.actor SET last_update = %s WHERE actor.actor_id = %s;"
        params = request.args.get('last_update', ''), actor_id
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Datos del actor actualizados con éxito"}, 200

    @app.route('/actors/<int:actor_id>', methods = ['DELETE'])
    def delete_actor(actor_id):
        query = "DELETE FROM sakila.actor WHERE actor.actor_id = %s;"
        params = actor_id,
        DatabaseConnection.execute_query(query, params)

        return {"msg": "Actor eliminado con éxito"}, 204

    @app.route('/actors/', methods = ['DELETE'])
    def delete_actors():
        query= "DELETE FROM sakila.actor;"
        DatabaseConnection.execute_query(query)
        return {"msg": "Actor eliminado con éxito"}, 200
    
    return app