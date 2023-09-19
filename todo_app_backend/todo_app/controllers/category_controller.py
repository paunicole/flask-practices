from flask import request
from ..models.category_model import Category

class CategoryController:

    @classmethod
    def get(cls):
        categories = Category.get()
        return [category.to_dict() for category in categories], 200

    @classmethod
    def get_by_id(cls, category_id):
        category_obj = Category(category_id=category_id)
        category = Category.get(category_obj)
        if category:
            return category.to_dict(), 200

    @classmethod
    def create(cls):
        data = request.json
        category_obj = Category(name=data['name'], description=data.get('description'))
        Category.create(category_obj)
        return {'message': 'Category created successfully'}, 201

    @classmethod
    def update(cls, category_id):
        data = request.json
        category_obj = Category(
            category_id=category_id,
            name=data.get('name'), 
            description=data.get('description')
            )
        Category.update(category_obj)
        return {'message': 'Category updated successfully'}, 200

    @classmethod
    def delete(cls, category_id):
        category_obj = Category(category_id=category_id)
        Category.delete(category_obj)
        return {'message': 'Category deleted successfully'}, 200
