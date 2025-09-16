from flask_restx import reqparse

parser = reqparse.RequestParser()

parser.add_argument('page', type=int, help='Page number', default=1)