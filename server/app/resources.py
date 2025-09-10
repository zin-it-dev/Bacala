from flask_restx import Resource, Namespace

from .dto import category
from .repositories import CategoryRepository

category_ns = Namespace('categories', description='Category operations')

@category_ns.route('/')
class CategoryList(Resource):
    @category_ns.doc('category_list')
    @category_ns.marshal_list_with(category)
    def get(self):
        '''List all categories'''
        return CategoryRepository().get_all()