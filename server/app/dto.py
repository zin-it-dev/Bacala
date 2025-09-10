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

category = api.model(
    "Category",
    {**common, 'name': fields.String(required=True, description='The category name')},
)