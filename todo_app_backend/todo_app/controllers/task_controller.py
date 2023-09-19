from flask import request
from ..models.task_model import Task

from ..models.exceptions import NotFound, BadRequest

class TaskController:

    @classmethod
    def get(cls):
        tasks = []
        if request.args.get('category_id'):
            task_obj = Task(category_id=request.args.get('category_id'))
            tasks = Task.get(task_obj)
        else:
            tasks = Task.get()
        return [task.to_dict() for task in tasks], 200

    @classmethod
    def get_by_id(cls, task_id):
        if task_id <= 0:
            raise BadRequest("El id de la tarea debe ser mayor a 0") 
        task_obj = Task(task_id=task_id)
        task = Task.get(task_obj)
        if task:
            return task.to_dict(), 200
        raise NotFound("Tarea no encontrada")

    @classmethod
    def create(cls):
        data = request.json
        task_obj = Task(
            name=data.get('name'),
            due_date=data.get('due_date'),
            category_id=data.get('category_id')
            )
        Task.create(task_obj)
        return {'message': 'Task created successfully'}, 201

    @classmethod
    def update(cls, task_id):
        data = request.json
        task_obj = Task(
            task_id=task_id,
            name=data.get('name'),
            due_date=data.get('due_date'),
            creation_date=data.get('creation_date'),
            completed=data.get('completed'),
            category_id=data.get('category_id')
        )
        Task.update(task_obj)
        return {'message': 'Task updated successfully'}, 200

    @classmethod
    def delete(cls, task_id):
        task_obj = Task(task_id=task_id)
        Task.delete(task_obj)
        return {'message': 'Task deleted successfully'}, 200