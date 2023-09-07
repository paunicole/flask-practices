from flask import jsonify

class UserNotFound(Exception):

    def __init__(self, description = "El ususario solicitado no existe"):
        super().__init__()
        self.description = description
        self.status_code = 401

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response

class DatabaseError(Exception):

    def __init__(self, description = "Error en la base de datos"):
        super().__init__()
        self.description = description
        self.status_code = 500

    def get_response(self):
        response = jsonify({
            'error': {
                'code': self.status_code,
                'description': self.description,
            }
        })
        response.status_code = self.status_code
        return response