from ..database import DatabaseConnection

class Brand:

    def __init__(self, **kwargs):
        self.brand_id = kwargs.get('brand_id')
        self.brand_name = kwargs.get('brand_name')
    
    def serialize(self):
        return {
            "brand_id": self.brand_id,
            "brand_name": self.brand_name
        }

    @classmethod
    def get_brand(cls, brand):
        query = """SELECT brand_id, brand_name FROM production.brands WHERE brand_id = %(brand_id)s"""
        params = brand.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return Brand(
                brand_id = result[0],
                brand_name = result[1]
            )
        return None