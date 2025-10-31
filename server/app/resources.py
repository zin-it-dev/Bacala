from flask_restx import Resource, Namespace, abort

from .dto import category, books, book, comments, comment
from .repositories import CategoryRepository, BookRepository, CommentRepository
from .extensions import cache
from .parsers import parser_book, parser_comment
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
    @book_ns.expect(parser_book)
    @cache.cached(timeout=60*2, query_string=True, key_prefix='book_list')
    def get(self):
        '''List all books'''
        args = parser_book.parse_args()
        return BookRepository().get_all(**args, page_size=StandardResultsSetPagination.page_size)
    
    
@book_ns.route("/<int:id>/")
@book_ns.response(404, "Book not found")
@book_ns.param("id", "The book identifier")
class BookRetrieve(Resource):
    @book_ns.doc("book_retrieve")
    @book_ns.marshal_with(book, code=200)
    def get(self, id):
        """Fetch a given resource"""
        return BookRepository().get_by_id(id) or abort(404, message=f"Book {id} doesn't exist")
 
 
 
@book_ns.route("/<int:id>/comments")
@book_ns.response(404, "Book not found")
@book_ns.param("id", "The book identifier")
class CommentList(Resource):   
    @book_ns.doc("comment_list")
    @book_ns.marshal_with(comments)
    @book_ns.expect(parser_comment)
    def get(self, id):
        """List all comments"""
        args = parser_comment.parse_args()
        if not BookRepository().get_by_id(id): 
            abort(404, message=f"Book {id} doesn't exist")
        return CommentRepository().get_all(id, **args, page_size=StandardResultsSetPagination.page_size)
    