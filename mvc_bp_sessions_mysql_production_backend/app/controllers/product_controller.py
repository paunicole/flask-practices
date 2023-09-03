from ..models.product_model import Product
from flask import request

class ProductController:

    @classmethod
    def create_product(self):
        data = request.json
        product = Product(
            product_name = data.get('product_name'),
            brand_id = data.get('brand_id'),
            category_id = data.get('category_id'),
            model_year = data.get('model_year'),
            list_price = data.get('list_price')
        )
        Product.create_product(product)
        return {}, 201

    @classmethod
    def update_product(self, product_id):
        data = request.json
        product = Product(
            product_id = product_id,
            product_name = data.get('product_name'),
            brand = data.get('brand_id'),
            category = data.get('category'),
            model_year = data.get('model_year'),
            list_price = data.get('list_price')
        )
        Product.update_product(product)
        return {}, 200

    @classmethod
    def get_products(self):
        products = [product.serialize() for product in Product.get_products()]
        return {"products": products, "total": len(products)}, 200

    @classmethod
    def get_product(self, product_id):
        return Product.get_product(Product(
            product_id = product_id
        )).serialize(), 200
    
    @classmethod
    def delete_product(self, product_id):
        Product.delete_product(Product(product_id = product_id))
        return {}, 204