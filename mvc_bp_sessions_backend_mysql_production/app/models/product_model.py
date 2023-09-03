from ..database import DatabaseConnection
from .product_category_model import Category
from .brand_model import Brand

class Product:

    def __init__(self, **kwargs):
        self.product_id = kwargs.get('product_id')
        self.product_name = kwargs.get('product_name')
        self.brand_id = kwargs.get('brand_id')
        self.category_id = kwargs.get('category_id')
        self.model_year = kwargs.get('model_year')
        self.list_price = kwargs.get('list_price')
    
    def serialize(self):
        return {
            "product_id": self.product_id,
            "product_name": self.product_name,
            "brand_id": Brand.get_brand(Brand(brand_id=self.brand_id)).serialize(),
            "category_id": Category.get_category(Category(category_id=self.category_id)).serialize(),
            "model_year": self.model_year,
            "list_price": self.list_price,
        }

    @classmethod
    def create_product(cls, product):
        query = """
        INSERT INTO
            production.products (product_name, brand_id, category_id, model_year, list_price)
        VALUES
            (%(product_name)s, %(brand_id)s, %(category_id)s, %(model_year)s, %(list_price)s);"""
        params = product.__dict__
        DatabaseConnection.execute_query(query, params=params)
    
    @classmethod
    def get_products(self):
        query = """
        SELECT
            products.product_id,
            products.product_name,
            products.brand_id,
            products.category_id,
            products.model_year,
            products.list_price
        FROM
            production.products;"""
        results = DatabaseConnection.fetch_all(query)
        products = []
        for result in results:
            products.append(Product(
                product_id = result[0],
                product_name = result[1],
                brand_id = result[2],
                category_id = result[3],
                model_year = result[4],
                list_price = result[5],
            ))
        return products

    @classmethod
    def get_product(cls, product):
        query = """
        SELECT
            products.product_id,
            products.product_name,
            products.brand_id,
            products.category_id,
            products.model_year,
            products.list_price
        FROM
            production.products
        WHERE
            product_id = %(product_id)s;"""
        params = product.__dict__
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                product_id = result[0],
                product_name = result[1],
                brand_id = result[2],
                category_id = result[3],
                model_year = result[4],
                list_price = result[5],
            )
        return None
    
    @classmethod
    def update_product(cls, product):
        pass

    @classmethod
    def delete_product(cls, product):
        query = """
        DELETE FROM
            production.products
        WHERE
            product_id = %(product_id)s;"""
        params = product.__dict__
        DatabaseConnection.execute_query(query, params=params)