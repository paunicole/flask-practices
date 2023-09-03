# Sessions Backend

1. Cargar la base de datos para probar el ejercicio. En la carpeta `tablas_db_para_workbench`. Crear la estructura utilizando open script. Cargar los datos, de la misma manera.

2. Crear un archivo llamado `.env` en la raíz del proyecto con la siguiente información:
   
   ```python
   SECRET_KEY = 352528b35a4cca7bf961c3f7c0dac9642c527428388d4de5f443df34f0e6e320
   DATABASE_USERNAME = 'root'
   DATABASE_PASSWORD = 'root'
   DATABASE_HOST = '127.0.0.1'
   DATABASE_PORT = '3306'
   ```
3. Instalar los siguientes módulos:
   ```
   pip install flask-cors
   pip install python-dotenv
   ```

5. Levantar el servidor local (dar al btón de play en la sección de Flask).

6. Luego abrir otra instancia de VSC y correr el frontend en el browser externo. Probar las credenciales Existentes de Joe y Admin.
