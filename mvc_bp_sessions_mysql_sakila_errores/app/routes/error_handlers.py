from flask import Blueprint
from ..models.exceptions import FilmNotFound

errors = Blueprint("errors", __name__)

# ======== Ejercicio 1 =========
@errors.app_errorhandler(FilmNotFound)
def handle_film_not_found(error):
    return error.get_response(), error.status_code