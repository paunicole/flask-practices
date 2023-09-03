from flask import Flask, request
from config import Config
from .database import DatabaseConnection

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)

    @app.route('/')
    def bienvenida():
        return 'Pagina de bienvenida'


    # ======== Ejercicio 1.1 ========
    @app.route('/customers/<int:customer_id>', methods = ['GET'])
    def get_customer(customer_id):
        query = "SELECT city, customer_id, email, first_name, last_name, phone, state, street, zip_code FROM sales.customers WHERE customer_id = %s;"
        params = customer_id,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return {
                "city": result[0],
                "customer_id": result[1],
                "email": result[2],
                "first_name": result[3],
                "last_name": result[4],
                "phone": result[5],
                "state": result[6],
                "street": result[7],
                "zip_code": result[8]
            }, 200
        return {"msg": "No se encontró el cliente"}, 404


    # ======== Ejercicio 1.2 ========
    @app.route('/customers', methods = ['GET'])
    def get_actors():
        query = "SELECT city, customer_id, email, first_name, last_name, phone, state, street, zip_code FROM sales.customers;"
        results = DatabaseConnection.fetch_all(query)
        customers = []
        for result in results:
            customers.append({
                "city": result[0],
                "customer_id": result[1],
                "email": result[2],
                "first_name": result[3],
                "last_name": result[4],
                "phone": result[5],
                "state": result[6],
                "street": result[7],
                "zip_code": result[8]
            })
        dict_customers = {
            "customers": customers,
            "total": len(results)
        }
        return dict_customers, 200


    # ======== Ejercicio 1.3 ========
    @app.route('/customers', methods = ['POST'])
    def create_actor():
        query= "INSERT INTO sales.customers (first_name, last_name, email) VALUES (%s,%s,%s);"
        params = request.args.get('first_name', ''), request.args.get('last_name', ''), request.args.get('email', '')
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Cliente creado con éxito"}, 201


    # ======== Ejercicio 1.4 ========
    @app.route('/customers/<int:customer_id>', methods = ['PUT'])
    def update_customer(customer_id):
        query = "UPDATE sales.customers SET first_name = %s WHERE customers.customer_id = %s;"
        params = request.args.get('first_name', ''), customer_id
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Datos del cliente actualizados con éxito"}, 200


    # ======== Ejercicio 1.5 ========
    @app.route('/customers/<int:customer_id>', methods = ['DELETE'])
    def delete_actor(actor_id):
        query = "DELETE FROM sales.customers WHERE customers.customer_id = %s;"
        params = actor_id,
        DatabaseConnection.execute_query(query, params)

        return {"msg": "Cliente eliminado con éxito"}, 204


    # ======== Ejercicio 2.1 ========
    @app.route('/products/<int:product_id>', methods = ['GET'])
    def get_product(product_id):
        query = """ SELECT brands.brand_id, brands.brand_name, categories.category_id, categories.category_name, products.list_price, products.model_year, products.product_id, products.product_name
        FROM production.categories
        INNER JOIN production.products
        ON categories.category_id = products.product_id
        INNER JOIN production.brands
        ON brands.brand_id = products.brand_id
        WHERE products.product_id = %s;"""
        params = product_id,
        result = DatabaseConnection.fetch_one(query, params)
        if result is not None:
            return {
                "brand": {
                    "brand_id": result[0],
                    "brand_name": result[1]
                },
                "category": {
                    "category_id": result[2],
                    "category_name": result[3]
                },
                "list_price": result[4],
                "model_year": result[5],
                "product_id": result[6],
                "product_name": result[7]
            }, 200
        return {"msg": "No se encontró el producto"}, 404


    # ======== Ejercicio 2.2 ========
    @app.route('/products', methods = ['GET'])
    def get_products():
        query = """ SELECT brands.brand_id, brands.brand_name, categories.category_id, categories.category_name, products.list_price, products.model_year, products.product_id, products.product_name
        FROM production.categories
        INNER JOIN production.products
        ON categories.category_id = products.product_id
        INNER JOIN production.brands
        ON brands.brand_id = products.brand_id;"""
        results = DatabaseConnection.fetch_all(query)
        products = []
        for result in results:
            products.append({
                "brand": {
                    "brand_id": result[0],
                    "brand_name": result[1]
                },
                "category": {
                    "category_id": result[2],
                    "category_name": result[3]
                },
                "list_price": result[4],
                "model_year": result[5],
                "product_id": result[6],
                "product_name": result[7]
            })
        dict_products = {
            "products": products,
            "total": len(results)
        }
        return dict_products, 200


    # ======== Ejercicio 2.3 ========
    @app.route('/customers', methods = ['POST'])
    def create_product():
        query= "INSERT INTO production.products (product_name, brand_id, category_id, model_year, list_price) VALUES (%s,%s,%s,%s,%s);"
        params = request.args.get('product_name', ''), request.args.get('brand_id', ''), request.args.get('category_id', ''), request.args.get('model_year', ''), request.args.get('list_price', '')
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Producto creado con éxito"}, 201


    # ======== Ejercicio 2.4 ========
    @app.route('/products/<int:product_id>', methods = ['PUT'])
    def update_customer(customer_id):
        query = "UPDATE production.products SET list_price = %s WHERE product_id = %s;"
        params = request.args.get('list_price', ''), customer_id
        DatabaseConnection.execute_query(query, params)
        return {"msg": "Datos del producto actualizados con éxito"}, 200


    # ======== Ejercicio 2.5 ========
    @app.route('/products/<int:product_id>', methods = ['DELETE'])
    def delete_product(product_id):
        query = "DELETE FROM production.products WHERE product_id = %s;"
        params = product_id,
        DatabaseConnection.execute_query(query, params)

        return {"msg": "Producto eliminado con éxito"}, 204


    return app