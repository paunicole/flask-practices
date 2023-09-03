from ..models.product_model import Product
from flask import request, jsonify

class ProductController:
    
    @classmethod
    def get_product(self, product_id):
        product_instance = Product.get_product(product_id) 
        
        if product_instance:
            response_data = {
                "brand": product_instance.brand,
                "category": product_instance.category,
                "list_price": product_instance.list_price,
                "model_year": product_instance.model_year,
                "product_id": product_instance.product_id,
                "product_name": product_instance.product_name
            }
            return jsonify(response_data), 200
    
    @classmethod
    def get_products(self):
        products_instance = Product.get_products()
        response = {
            'Customers': products_instance,
            'Total': len(products_instance)
        }
        return jsonify(response), 200

    @classmethod
    def create_product(self):
        product = Product(
            product_id = None, 
            product_name = request.args.get('product_name'),
            brand = request.args.get('brand_id'),
            category = request.args.get('category_id'),
            model_year = request.args.get('model_year'),
            list_price = request.args.get('list_price')
        )
        Product.create_product(product)
        return {}, 201

    @classmethod
    def update_product(self, product_id):
        pass

    @classmethod
    def delete_product(self, product_id):
        Product.delete_product(product_id)
        return {}, 204