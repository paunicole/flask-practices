from flask import request
from ..models.task_item_model import TaskItem

class TaskItemController:

    @classmethod
    def get(cls):
        task_items = []
        if request.args.get('task_id'):
            task_item_obj = TaskItem(task_id=request.args.get('task_id'))
            task_items = TaskItem.get(task_item_obj)
        else:
            task_items = TaskItem.get()
        return [task_item.to_dict() for task_item in task_items], 200

    @classmethod
    def get_by_id(cls, ti_id):
        task_item_obj = TaskItem(ti_id=ti_id)
        task_item = TaskItem.get(task_item_obj)
        if task_item:
            return task_item.to_dict(), 200

    @classmethod
    def create(cls):
        data = request.json
        task_item_obj = TaskItem(item=data['item'], task_id=data['task_id'])
        TaskItem.create(task_item_obj)
        return {'message': 'Task item created successfully'}, 201

    @classmethod
    def update(cls, ti_id):
        data = request.json
        task_item_obj = TaskItem(
            ti_id=ti_id,
            item=data.get('item', None),
            task_id=data.get('task_id'),
            completed=data.get('completed', False)
            )
        TaskItem.update(task_item_obj)
        return {'message': 'Task item updated successfully'}, 200

    @classmethod
    def delete(cls, ti_id):
        task_item_obj = TaskItem(ti_id=ti_id)
        TaskItem.delete(task_item_obj)
        return {'message': 'Task item deleted successfully'}, 200