from flask_restx import Resource, Namespace

from .dto import category, books, book
from .repositories import CategoryRepository, BookRepository
from .extensions import cache
from .parsers import parser
from .paginatiors import StandardResultsSetPagination

category_ns = Namespace('categories', description='Category operations')
book_ns = Namespace('books', description='Book operations')

@category_ns.route('/')
class CategoryList(Resource):
    @category_ns.doc('category_list')
    @category_ns.marshal_list_with(category)
    @cache.cached(timeout=60*2, key_prefix='category_list')
    def get(self):
        '''List all categories'''
        return CategoryRepository().get_all()
    
    
@book_ns.route('/')
class BookList(Resource):
    @book_ns.doc('book_list')
    @book_ns.marshal_with(books)
    @book_ns.expect(parser)
    @cache.cached(timeout=60*2, query_string=True, key_prefix='book_list')
    def get(self):
        '''List all books'''
        args = parser.parse_args()
        return BookRepository().get_all(**args, page_size=StandardResultsSetPagination.page_size)