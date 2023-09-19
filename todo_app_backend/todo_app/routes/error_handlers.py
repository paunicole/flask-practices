from flask import Blueprint, json
from ..models.exceptions import *

errors = Blueprint("errors", __name__)

@errors.app_errorhandler(BadRequest)
def handle_bad_request(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(NotFound)
def handle_not_found(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(InternalServerError)
def handle_internal_server_error(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(MethodNotAllowed)
def handle_method_not_allowed(error):
    return error.get_response(), error.status_code

@errors.app_errorhandler(404)
def handle_werkzeug_bad_request(error):
    """Manejador de errores para el error 404 de Werkzeug"""

    response = error.get_response()
    # Reemplazamos el contenido de la respuesta por un JSON
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": "La URL solicitada no existe. Por favor, revise la URL e intente nuevamente."
    })
    response.content_type = "application/json"
    return response

@errors.app_errorhandler(405)
def handle_werkzeug_method_not_allowed(error):
    """Manejador de errores para el error 405 de Werkzeug"""

    response = error.get_response()
    # Reemplazamos el contenido de la respuesta por un JSON
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": "El método HTTP utilizado no está permitido para la URL solicitada."
    })
    response.content_type = "application/json"
    return response