from ..models.staff_model import Staff
from flask import json

from flask import request

class StaffController:

    @classmethod
    def create_staff(self):
        data = request.json
        staff = Staff(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            email = data.get('email'),
            phone = data.get('phone'),
            manager_id = data.get('manager_id'),
            active = data.get('active'),
            store_id = data.get('store_id')
        )
        Staff.create_staff(staff)

        return {}, 201
    
    @classmethod
    def get_staff(self, staff_id):
        staff = Staff(staff_id=staff_id)
        staff = Staff.get_staff(staff)

        return staff.__dict__, 200
    
    @classmethod
    def get_staffs(self):
        staffs = Staff.get_staff_list()
        staffs_members = []
        for staff in staffs:
            staffs_members.append(staff.__dict__)

        return staffs_members, 200
    
    @classmethod
    def update_staff(self, staff_id):
        data = request.json
        staff = Staff(
            staff_id = staff_id,
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            email = data.get('email'),
            phone = data.get('phone'),
            manager_id = data.get('manager_id'),
            active = data.get('active'),
            store_id = data.get('store_id')
        )
        Staff.update_staff(staff)

        return {}, 200
    
    @classmethod
    def delete_staff(self, staff_id):
        staff = Staff(staff_id=staff_id)
        Staff.delete_staff(staff)

        return {}, 200