from ..database import DatabaseConnection

class Category:

    def __init__(self, **kwargs):
        self.category_id = kwargs.get('category_id')
        self.category_name = kwargs.get('category_name')
    
    def serialize(self):
        return {
            "category_id": self.category_id,
            "category_name": self.category_name
        }

    @classmethod
    def get_category(cls, category):
        query = """SELECT category_id, category_name FROM production.categories WHERE category_id = %(category_id)s"""
        params = category.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return Category(
                status_id = result[0],
                status_name = result[1]
            )
        return None