from flask import jsonify

class CustomException(Exception):

    def __init__(self, status_code, name = "Custom Error", description = 'Error'): 
        super().__init__()
        self.description = description
        self.name = name
        self.status_code = status_code

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'name': self.name,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class BadRequest(CustomException):

    def __init__(self, description = 'Solcitud inválida'):
        super().__init__(400, name = "Bad Request", description = description)
    
class NotFound(CustomException):

    def __init__(self, description = 'Recurso no encontrado'):
        super().__init__(404, name = "Not Found", description = description)

class InternalServerError(CustomException):

    def __init__(self, description = 'Error interno del servidor'):
        super().__init__(500, name = "Internal Server Error", description = description)

class MethodNotAllowed(CustomException):

    def __init__(self, description = 'Método no permitido'):
        super().__init__(405, name = "Method Not Allowed", description = description)