from flask_restx import Resource, Namespace

user_ns = Namespace('users', description='Users related operations')


@user_ns.route('/')
class UserResource(Resource):
    """
    Resource for handling individual user operations.
    Each method corresponds to an HTTP verb.
    """
    
    def get(self):
        return {"hello": "world"}
    
    