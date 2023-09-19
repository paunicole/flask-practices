from flask import Blueprint
from ..models.exceptions import FilmNotFound, InvalidDataError

errors = Blueprint("errors", __name__)

# ======== Ejercicio 1, 3, 5 =========
@errors.app_errorhandler(FilmNotFound)
def handle_film_not_found(error):
    return error.get_response(), error.status_code

# ======== Ejercicio 2, 4 =========
@errors.app_errorhandler(InvalidDataError)
def handle_invalid_data_error(error):
    return error.get_response(), error.status_code