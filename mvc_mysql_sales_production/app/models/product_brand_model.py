from ..database import DatabaseConnection

class ProductBrand:
    def __init__(self, brand_id, brand_name):
        self.brand_id = brand_id
        self.brand_name = brand_name
    
    @classmethod
    def get(cls, brand_id):
        query = """SELECT brand_id, brand_name FROM production.brands WHERE brand_id = %s"""
        params = (brand_id,)
        result = DatabaseConnection.fetch_one(query, params)

        if result is not None:
            return ProductBrand(
                brand_id = result[0],
                brand_name = result[1]
            )
        return None