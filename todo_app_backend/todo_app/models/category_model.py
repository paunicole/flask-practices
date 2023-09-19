from ..connection import DatabaseConnection

class Category:
    _keys = ('category_id', 'name', 'description')
    
    def __init__(self, **kwargs):
        self.category_id = kwargs.get('category_id')
        self.name = kwargs.get('name')
        self.description = kwargs.get('description')

    def to_dict(self):
        return self.__dict__

    @classmethod
    def create(cls, category):
        query = "INSERT INTO categories (name, description) VALUES (%s, %s)"
        params = (category.name, category.description)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, category):
        query = "DELETE FROM categories WHERE category_id = %s"
        params = (category.category_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get(cls, category = None):
        if category and category.category_id:
            query = "SELECT category_id, name, description FROM categories WHERE category_id = %s"
            params = (category.category_id,)
            result = DatabaseConnection.fetch_one(query, params)
            return cls(**dict(zip(cls._keys, result))) if result else None
        else:
            query = "SELECT category_id, name, description FROM categories"
            results = DatabaseConnection.fetch_all(query)
            return [cls(**dict(zip(cls._keys, row))) for row in results]

    @classmethod
    def update(cls, category):
        allowed_columns = {'name', 'description'}
        query_parts = []
        params = []
        for key, value in category.to_dict().items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        
        params.append(category.category_id)
        query = "UPDATE categories SET " + ", ".join(query_parts) + " WHERE category_id = %s"
        DatabaseConnection.execute_query(query, params)