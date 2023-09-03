from ..database import DatabaseConnection
from .product_category_model import ProductCategory
from .product_brand_model import ProductBrand

class Product:
    def __init__(self, product_id=None, product_name=None, brand=None, category=None, model_year=None, list_price=None):
        self.product_id = product_id
        self.product_name = product_name
        self.brand = brand
        self.category = category
        self.model_year = model_year
        self.list_price = list_price

    @classmethod
    def get_product(cls, producto_id):
        query = '''
        SELECT
            product_id,
            product_name,
            brand_id,
            category_id,
            model_year,
            list_price
        FROM
            production.products
        WHERE
            product_id = %s;
        '''
        params = (producto_id,)
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            brand = ProductBrand.get(result[2])
            category = ProductCategory.get(result[3])
            return Product(
                product_id=result[0],
                product_name=result[1],
                brand={"brand_id": brand.brand_id, "brand_name": brand.brand_name},
                category={"category_id": category.category_id, "category_name": category.category_name},
                model_year=result[4],
                list_price=result[5]
            )
        else:
            return None

    @classmethod
    def create_product(cls, product):
        query = '''
        INSERT INTO production.products (product_name, brand_id, category_id, model_year, list_price)
        VALUES (%s, %s, %s, %s, %s);
        '''
        params = (product.product_name, product.brand, product.category, product.model_year, product.list_price)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_products(cls):
        query = '''
        SELECT
            product_id,
            product_name,
            brand_id,
            category_id,
            model_year,
            list_price
        FROM
            production.products;
        '''
        results = DatabaseConnection.fetch_all(query)
        products_list = []

        for result in results:
            brand = ProductBrand.get(result[2])
            category = ProductCategory.get(result[3])
            products_list.append({
                "product_id": result[0],
                "product_name": result[1],
                "brand": {"brand_id": brand.brand_id, "brand_name": brand.brand_name},
                "category": {"category_id": category.category_id, "category_name": category.category_name},
                "model_year": result[4],
                "list_price": result[5]
            })

        return products_list
    
    @classmethod
    def update_product(cls, producto_id):
        pass
    
    @classmethod
    def delete_product(cls, producto_id):
        query = "DELETE FROM production.products WHERE product_id = %s;"
        params = (producto_id,)
        DatabaseConnection.execute_query(query, params)