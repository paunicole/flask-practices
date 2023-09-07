## Ejercicio de manejo de errores utilizando la base de datos de SALES de Bikestore

### Vamos a realizar los siguientes endpoints con bp: 

*#Crear staff con metodo post -> controlador create_staff*
staff_bp.route('/', methods = ['POST'])(StaffController.create_staff)<br>**Manejar error:  DatabaseError("No se pudo crear al nuevo miembro del staff")**

*#Actualizar staff con metodo put -> Controlador update_staff*
staff_bp.route('/<int:staff_id>', methods = ['PUT'])(StaffController.update_staff)

*#Obtener staff  con metodo get -> controlador get_staffs*
staff_bp.route('/', methods = ['GET'])(StaffController.get_staffs)

*#Obtener staff con id con metodo get -> controaldor get_staff*
staff_bp.route('/<int:staff_id>', methods = ['GET'])(StaffController.get_staff)<br>**Manejar error de UserNotFound("El usuario solicitado no existe")**

*#Eliminar staff con id con metodo delete -> Controlador delete_staff*
staff_bp.route('/<int:staff_id>', methods = ['DELETE'])(StaffController.delete_staff)<br>**Manejar error: DatabaseError("No se pudo eliminar al staff")**

Recordar que se debe crear en la carpeta modelo un archivo exceptions.py donde tendremos tantas clases como manejo de errores necesitemos, para este ejmplo dos:
- class UserNotFound(Exception)
- class DatabaseError(Exception)

Utilizar Thunder Client de las extensiones de VSC para probar Get, Put,Delete, Post