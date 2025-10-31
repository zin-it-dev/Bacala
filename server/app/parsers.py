from flask_restx import reqparse

parser = reqparse.RequestParser()
parser.add_argument('page', type=int, help='Page number', default=1)

parser_book = parser.copy()

parser_book.add_argument(
    "category", type=int, required=False, help="Category ID", location="args"
)
parser_book.add_argument(
    "keyword", type=str, required=False, help="Search keyword", location="args"
)

parser_comment = parser.copy()

