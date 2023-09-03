from ..database import DatabaseConnection

class ProductCategory:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name
    
    @classmethod
    def get(cls, category_id):
        query = """SELECT category_id, category_name FROM production.categories WHERE category_id = %s"""
        params = (category_id,)
        result = DatabaseConnection.fetch_one(query, params)

        if result is not None:
            return ProductCategory(
                category_id = result[0],
                category_name = result[1]
            )
        return None