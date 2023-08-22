from flask import Flask, request, render_template
from config import Config
import csv

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            return logearse()
        else:
            return mostrar_formulario()

    @app.post('/login')
    def login_post():
        return logearse()

    @app.get('/login')
    def login_get():
        return mostrar_formulario()

    def mostrar_formulario():
        return render_template('formulario_login.html')

    def logearse():
        usuarios = obtener_usuarios()
        nombre = request.form['nombre']
        contrasena = request.form['contrasena']
        if usuarios.get(nombre) == contrasena:
            return "Inicio de sesión exitoso"
        else:
            return "Error: Nombre de usuario o contraseña incorrectos"

    def obtener_usuarios():
        usuarios = {}
        with open('usuarios.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader) # Saltamos la primera fila (cabecera)
            for row in reader:
                usuarios[row[0]] = row[1]

        return usuarios

    return app