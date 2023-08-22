from flask import Flask, jsonify, request
from config import Config
from datetime import datetime
import json

def init_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__, static_folder = Config.STATIC_FOLDER, template_folder = Config.TEMPLATE_FOLDER)
    app.config.from_object(Config)
    
    # Ejercicio 1
    @app.route('/')
    def bienvenida():
        return 'Bienvenidx!'

    # Ejercicio 2
    @app.route('/info')
    def info():
        return f'Bienvenidx a {Config.APP_NAME}'

    # Ejercicio 3
    @app.route('/about')
    def about():
        diccionario = {
            'app_name': Config.APP_NAME,
            'description': Config.DESCRIPTION,
            'developers': Config.DEVELOPERS,
            'version': Config.VERSION
        }
        return diccionario

    # Ejercicio 4
    @app.route('/sum/<int:num1>/<int:num2>')
    def suma(num1, num2):
        return f'{num1 + num2}'

    # Ejercicio 5
    @app.route('/age/<dob>')
    def calcular_edad(dob):
        try:
            fecha_nacimiento = datetime.strptime(dob, "%Y-%m-%d")
            fecha_actual = datetime.now()
            
            if fecha_nacimiento > fecha_actual:
                error_message = {"error": "La fecha de nacimiento es posterior a la fecha actual."}
                return ({"error": "La fecha de nacimiento es posterior a la fecha actual."}, 400, {'Content-Type':'text/json; charset=utf-8'})
            
            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            return jsonify({"age": edad})
        except ValueError:
            error_message = {"error": "Formato de fecha incorrecto. Utilice el formato ISO 8601 (YYYY-MM-DD)."}
            return (error_message, 400, {'Content-Type':'text/json; charset=utf-8'})
            #return jsonify(error_message), 400

    # Ejericio 6
    @app.route('/operate/<string:operation>/<int:num1>/<int:num2>')
    def operacion(operation, num1, num2):
        if operation == 'sum':
            resultado = num1 + num2
        elif operation == 'sub':
            resultado = num1 - num2
        elif operation == 'mult':
            resultado = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return jsonify({"error": "La división no está definida para divisor igual a 0."}), 400
            resultado = num1 / num2
        else:
            return jsonify({"error": "Operación no válida. Las operaciones válidas son: sum, sub, mult, div."}), 400
        
        return jsonify({"resultado": resultado})

    # Ejericio 7
    @app.route('/operate')
    def realizar_operacion_query():
        operation = request.args.get('operation')
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))

        if operation == 'sum':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mult':
            result = num1 * num2
        elif operation == 'div':
            if num2 == 0:
                return jsonify({"error": "La división no está definida para divisor igual a 0."}), 400
            result = num1 / num2
        else:
            return jsonify({"error": "Operación no válida. Las operaciones válidas son: sum, sub, mult, div."}), 400
        
        return jsonify({"result": result})

    # Ejercicio 8
    @app.route('/title/<string:word>')
    def formatear_titulo(word):
        formatted_word = word.capitalize()
        return jsonify({"formatted_word": formatted_word})

    # Ejercicio 9
    @app.route('/formatted/<string:dni>')
    def convertir_dni_a_entero(dni):
        dni_digits = ""
        for char in dni:
            if char.isdigit():
                dni_digits += char
        
        if len(dni_digits) != 8 or dni_digits[0] == '0':
            return jsonify({"error": "El DNI debe tener exactamente 8 dígitos y empezar con un digito distinto de 0."}), 400
        
        formatted_dni = int(dni_digits)
        return jsonify({"formatted_dni": formatted_dni})

    # Ejercicio 10
    @app.route('/format')
    def format_user_data():
        firstname = request.args.get('firstname')
        lastname = request.args.get('lastname')
        dob = request.args.get('dob')
        dni = request.args.get('dni')

        # Formatear nombre y apellido
        formatted_firstname = firstname.capitalize()
        formatted_lastname = lastname.capitalize()

        # Calcular edad
        try:
            fecha_nacimiento = datetime.strptime(dob, "%Y-%m-%d")
            fecha_actual = datetime.now()

            if fecha_nacimiento > fecha_actual:
                return jsonify({"error": "La fecha de nacimiento es posterior a la fecha actual."}), 400

            edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        except ValueError:
            return jsonify({"error": "Formato de fecha incorrecto. Utilice el formato ISO 8601 (YYYY-MM-DD)."}), 400

        # Formatear DNI
        dni_digits = ''.join(filter(str.isdigit, dni))

        if len(dni_digits) != 8 or dni_digits[0] == '0':
            return jsonify({"error": "El DNI debe tener exactamente 8 dígitos y empezar con un digito distinto de 0."}), 400

        formatted_dni = int(dni_digits)

        response_data = {
            "firstname": formatted_firstname,
            "lastname": formatted_lastname,
            "age": edad,
            "dni": formatted_dni
        }

        return jsonify(response_data)
    
    # Ejercicio 11
    @app.route('/encode/<string:keyword>')
    def encriptar(keyword):
        with open("hola_mundo/static/morse_code.json") as archivo:
            codigo_morse = json.load(archivo)
        codigos = codigo_morse["letters"]
        frase_encriptada = ''
        for caracter in keyword:
            print(caracter)
            if caracter.isalpha():
                caracter = caracter.upper()
            if caracter == '+':
                caracter = ' '
            if caracter in codigos:
                frase_encriptada += codigos[caracter] + '+'
        return frase_encriptada

    # Ejercicio 12
    @app.route('/decode/<string:morse_code>')
    def desencriptar(morse_code):
        frase_codigos = morse_code.split('+')

        with open("hola_mundo/static/morse_code.json") as archivo:
            codigo_morse = json.load(archivo)
        
        codigos = codigo_morse["letters"]

        frase_desencriptada = ''
        for codigo in frase_codigos:
            for k, v in codigos.items():
                if codigo == v:
                    frase_desencriptada += k
        return frase_desencriptada

    # Ejercicio 13
    @app.route('/convert/binary/<string:num>')
    def conversion(num):
        try:
            decimal_num = 0
            n = len(num)
            
            for i in range(n):
                if num[i] == '1':
                    decimal_num += int(num[i]) * (2 ** (n - 1 - i))
            return str(decimal_num)
        except ValueError:
            return "Error: El número binario ingresado es inválido."

    # Ejercicio 14
    @app.route('/balance/<string:input>')
    def balanceados(input):
        simbolos_apertura = ["[","{","("]
        simbolos_cierre = ["]","}",")"]
        stack = []
        for i in input:
            if i in simbolos_apertura:
                stack.append(i)
            elif i in simbolos_cierre:
                pos = simbolos_cierre.index(i)
                if ((len(stack) > 0) and
                    (simbolos_apertura[pos] == stack[len(stack)-1])):
                    stack.pop()
                else:
                    return jsonify({"balanced": False})

        if len(stack) == 0:
            return jsonify({"balanced": True})
        else:
            return jsonify({"balanced": False})

    return app