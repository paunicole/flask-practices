from ..connection import DatabaseConnection
from .category_model import Category
from .task_item_model import TaskItem

class Task:
    _keys = ('task_id', 'name', 'due_date', 'creation_date', 'completed', 'category_id')

    def __init__(self, **kwargs):
        self.task_id = kwargs.get('task_id')
        self.name = kwargs.get('name')
        self.due_date = kwargs.get('due_date')
        self.creation_date = kwargs.get('creation_date')
        self.completed = bool(kwargs.get('completed', False))
        self.category_id = kwargs.get('category_id')

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'name': self.name,
            'due_date': self.due_date,
            'creation_date': self.creation_date,
            'completed': self.completed,
            'category': Category.get(Category(category_id=self.category_id)).to_dict() if self.category_id else None,
            'task_items': [task_item.to_dict() for task_item in TaskItem.get(TaskItem(task_id=self.task_id))]
        }

    @classmethod
    def create(cls, task):
        query = "INSERT INTO tasks (name, due_date, creation_date, completed, category_id) VALUES (%s, %s, CURDATE(), %s, %s)"
        params = (task.name, task.due_date, task.completed, task.category_id)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, task):
        query = "DELETE FROM tasks WHERE task_id = %s"
        params = (task.task_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get(cls, task = None):
        if task and task.task_id:
            query = "SELECT task_id, name, due_date, creation_date, completed, category_id FROM tasks WHERE task_id = %s ORDER BY due_date ASC"
            params = (task.task_id,)
            result = DatabaseConnection.fetch_one(query, params)
            return cls(**dict(zip(cls._keys, result))) if result else None
        elif task and task.category_id:
            query = "SELECT task_id, name, due_date, creation_date, completed, category_id FROM tasks WHERE category_id = %s ORDER BY due_date ASC"
            params = (task.category_id,)
            results = DatabaseConnection.fetch_all(query, params)
            return [cls(**dict(zip(cls._keys, row))) for row in results]
        else:
            query = "SELECT task_id, name, due_date, creation_date, completed, category_id FROM tasks ORDER BY due_date ASC"
            results = DatabaseConnection.fetch_all(query)
            return [cls(**dict(zip(cls._keys, row))) for row in results]

    @classmethod
    def update(cls, task):
        allowed_columns = {'name', 'due_date', 'completed', 'category_id'}
        query_parts = []
        params = []
        for key, value in task.to_dict().items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        
        params.append(task.task_id)

        query = "UPDATE tasks SET " + ", ".join(query_parts) + " WHERE task_id = %s"
        DatabaseConnection.execute_query(query, params)