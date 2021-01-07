from flask_restplus import Namespace, fields

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


class RoleDto:
    api = Namespace('roles', authorizations=authorizations, description='Role related operations')

    RolePost = api.model('RolePost', {
        'role': fields.String()
    })

    RoleGetAll = api.model('RoleGetAll', {
        'publicId': fields.String,
        'role': fields.String()
    })

    RoleId = api.model('RoleId', {
        'publicId': fields.String,
    })
