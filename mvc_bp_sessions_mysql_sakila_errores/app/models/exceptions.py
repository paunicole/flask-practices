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


# =========== Ejercicio 1, 3, 5 ============
class FilmNotFound(CustomException):

    def __init__(self, description = 'El film solicitado no existe'): 
        super().__init__(404, "Film Not Found", description)


# =========== Ejercicio 2, 4 ============
class InvalidDataError(CustomException):

    def __init__(self, description = 'Dato no válido'): 
        super().__init__(400, "Invalid Data Error", description)