from ..connection import DatabaseConnection

class TaskItem:
    _keys = ('ti_id', 'item', 'task_id', 'completed')

    def __init__(self, **kwargs):
        self.ti_id = kwargs.get('ti_id')
        self.item = kwargs.get('item')
        self.task_id = kwargs.get('task_id')
        self.completed = bool(kwargs.get('completed', False))

    def to_dict(self):
        return self.__dict__

    @classmethod
    def create(cls, task_item):
        query = "INSERT INTO task_items (item, task_id, completed) VALUES (%s, %s, %s)"
        params = (task_item.item, task_item.task_id, task_item.completed)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def delete(cls, task_item):
        query = "DELETE FROM task_items WHERE ti_id = %s"
        params = (task_item.ti_id,)
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get(cls, task_item = None):
        if task_item and task_item.ti_id:
            query = "SELECT ti_id, item, task_id, completed FROM task_items WHERE ti_id = %s"
            params = (task_item.ti_id,)
            result = DatabaseConnection.fetch_one(query, params)
            return cls(**dict(zip(cls._keys, result))) if result else None
        elif task_item and task_item.task_id:
            query = "SELECT ti_id, item, task_id, completed FROM task_items WHERE task_id = %s"
            params = (task_item.task_id,)
            results = DatabaseConnection.fetch_all(query, params)
            return [cls(**dict(zip(cls._keys, row))) for row in results]
        else:
            query = "SELECT ti_id, item, task_id, completed FROM task_items"
            results = DatabaseConnection.fetch_all(query)
            return [cls(**dict(zip(cls._keys, row))) for row in results]

    @classmethod
    def update(cls, task_item):
        allowed_columns = {'item', 'completed'}
        query_parts = []
        params = []
        for key, value in task_item.to_dict().items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        
        # Add the task_item ID to be updated to the params list
        params.append(task_item.ti_id)

        query = "UPDATE task_items SET " + ", ".join(query_parts) + " WHERE ti_id = %s"

        DatabaseConnection.execute_query(query, tuple(params))