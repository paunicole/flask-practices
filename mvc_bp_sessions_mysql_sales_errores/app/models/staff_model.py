from ..database import DatabaseConnection
from .exceptions import DatabaseError, UserNotFound

class Staff:

    def __init__(self, staff_id = None, first_name = None, last_name = None, email = None, phone = None, active = None, store_id = None, manager_id = None):
        self.staff_id = staff_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.active = active
        self.store_id = store_id
        self.manager_id = manager_id
    
    @classmethod
    def get_staff(cls, staff):
        query = """SELECT staff_id, first_name, last_name, email, phone, active, store_id, manager_id 
            FROM sales.staffs
            WHERE staff_id = %s"""
        params = staff.staff_id,
        result = DatabaseConnection.fetch_one(query, params=params)
        if result is not None:
            return Staff(
                    staff_id = result[0],
                    first_name = result[1],
                    last_name = result[2],
                    email = result[3],
                    phone = result[4],
                    active = result[5],
                    store_id = result[6],
                    manager_id = result[7]
                )
        else:
            raise UserNotFound("El usuario solicitado no existe")

    @classmethod
    def get_staff_list(cls):
        query = """SELECT staff_id, first_name, last_name, email, phone, active, store_id, manager_id 
        FROM sales.staffs"""
        results = DatabaseConnection.fetch_all(query)
        staff_list = []
        for result in results:
            staff_list.append(Staff(
                staff_id = result[0],
                first_name = result[1],
                last_name = result[2],
                email = result[3],
                phone = result[4],
                active = result[5],
                store_id = result[6],
                manager_id = result[7]
            ))
        return staff_list
    
    @classmethod
    def create_staff(cls, staff):
        query = """INSERT INTO sales.staffs (first_name, last_name, email, phone, active, store_id, manager_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        params = staff.first_name, staff.last_name, staff.email, staff.phone, staff.active, staff.store_id, staff.manager_id
        cursor = DatabaseConnection.execute_query(query, params=params)
        
        if cursor.rowcount == 1:
            staff_id = cursor.lastrowid
            return staff_id
        else:
            raise DatabaseError("No se pudo crear al nuevo miembro del staff")

    @classmethod
    def delete_staff(cls, staff):
        query = """DELETE FROM sales.staffs WHERE staff_id = %s"""
        params = staff.staff_id,
        cursor = DatabaseConnection.execute_query(query, params=params)

        if cursor.rowcount == 0:
            raise DatabaseError("No se pudo eliminar al staff")
        else:
            return {"message": "Saff eliminado con exito"}
    
    @classmethod
    def update_staff(cls, staff):
        query = "UPDATE sales.staffs SET "
        staff_data = staff.__dict__
        staff_values = []
        staff_updates = []
        for key in staff_data.keys():
            if key != "staff_id" and staff_data[key] is not None:
                staff_updates.append(f"{key} = %s")
                staff_values.append(staff_data[key])
        query += ", ".join(staff_updates)
        query += " WHERE staff_id = %s"
        staff_values.append(staff.staff_id)
        params = tuple(staff_values)
        DatabaseConnection.execute_query(query, params=params)
        