from flask_restplus import Namespace, fields
# from app.main.service.constants import *

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


class UserDto:
    api = Namespace('user', authorizations=authorizations, description='User related operation')

    Name = api.model('Name', {
        'firstName': fields.String(),
        'lastName': fields.String(),
    })

    UserPost = api.model('UserPost', {
        'username': fields.String(),
        'name': fields.Nested(Name),
        'age': fields.Integer(),
        'email': fields.String(),
        'phone': fields.List(fields.String()),
        'roleId': fields.String(),
    })

    RoleGet = api.model('RoleGet', {
        'role': fields.String(),
    })

    UsersGetAll = api.model('UsersGetAll', {
        'publicId': fields.String(),
        'username': fields.String(),
        'name': fields.Nested(Name),
        'fullName': fields.String(),
        'age': fields.Integer(),
        'email': fields.String(),
        'phone': fields.List(fields.String()),
        'roleId': fields.List(fields.Nested(RoleGet)),
        'status': fields.String()
    })