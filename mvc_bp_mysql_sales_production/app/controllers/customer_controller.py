from ..models.customer_model import Customer
from flask import request

class CustomerController:
    
    @classmethod
    def get_customer(self, customer_id):
        Customer(customer_id = request.args.get('customer_id'))
        cust = Customer.get_customer(customer_id)
        return cust
    
    @classmethod
    def get_customers(self):
        cust = Customer.get_customers()
        response = {
            'Customers': cust,
            'Total': len(cust)
        }
        return response, 200
    
    def create_customer(self):
        cust = Customer(
            first_name = request.args.get('first_name', ''),
            last_name = request.args.get('last_name', ''),
            email = request.args.get('email', ''),
            phone = request.args.get('phone', ''),
            street = request.args.get('street', ''),
            city = request.args.get('city', ''),
            state = request.args.get('state', ''),
            zip_code = request.args.get('zip_code', ''),
        )
        Customer.create_customer(cust) 
        return {'msg': 'El cliente se ha creado con éxito'}, 201

    @classmethod
    def update_customer(self, first_name, last_name, email, phone, street, city, state, zip_code, customer_id):
        Customer(first_name = request.args.get('first_name'),
            last_name = request.args.get('last_name'),
            email = request.args.get('email'),
            phone = request.args.get('phone'),
            street = request.args.get('street'),
            city = request.args.get('city'),
            state = request.args.get('state'),
            zip_code = request.args.get('zip_code'),
            customer_id = request.args.get('customer_id',
            ))
        Customer.update_customer(first_name, last_name, email, phone, street, city, state, zip_code, customer_id)
        return {'msg': 'Cliente modificado con éxito'}, 200

    @classmethod
    def delete_customer(self, customer_id):
        Customer(customer_id = request.args.get('customer_id'))
        Customer.delete_customer(customer_id)
        return {'msg': 'El cliente fue eliminado con éxito'}, 204