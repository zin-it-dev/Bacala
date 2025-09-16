from flask_restx import fields

from . import api

common = api.model(
    "Common",
    {
        "id": fields.Integer(readonly=True, description="Unique ID"),
        "active": fields.Boolean,
        "date_created": fields.DateTime(dt_format="iso8601"),
    },
)

paginate = api.model(
    "Pagination",
    {
        "page_size": fields.Integer(description="Number of items per page"),
        "count": fields.Integer(description="Total number of items")
    }
)

category = api.model(
    "Category",
    {**common, 'name': fields.String(required=True, description='The category name')}
)

book = api.model(
    "Book",
    {
        **common, 
        'name': fields.String(required=True, description='The book name'),
        'description': fields.String(required=True, description='The book description'),
        "image": fields.String,
        "price": fields.Float
    }
)

books = api.model(
    "Books",
    {
        **paginate,
        "results": fields.List(fields.Nested(book)),
    }
)