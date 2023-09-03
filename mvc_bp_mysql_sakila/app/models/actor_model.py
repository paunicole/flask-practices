from ..database import DatabaseConnection

class Actor:
    def __init__(self, actor_id = None, first_name = None, last_name = None, last_update = None):
        self.actor_id = actor_id
        self.first_name = first_name
        self.last_name = last_name
        self.last_update = last_update

    @classmethod
    def create_actor(cls, actor):
        query = "INSERT INTO sakila.actor (first_name, last_name, last_update) VALUES (%s,%s,%s);"
        params = (actor.first_name, actor.last_name, actor.last_update)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_actor(actor):
        query = "SELECT first_name, last_name, last_update FROM sakila.actor WHERE actor_id = %s;"
        params = (actor.actor_id,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return Actor(
            actor_id = actor.actor_id,
            first_name = result[1],
            last_name = result[2],
            last_update = result[3]
            )
        else:
            return None