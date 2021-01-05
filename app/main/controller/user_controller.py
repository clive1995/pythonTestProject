from ..service.user_service import insert_user, fetch_user
# from app.main.util.roles.
from ..util.user_dto import UserDto
from app.main.service.constants import *
from flask_restplus import Resource
from flask import request
from flask_restplus import reqparse

api = UserDto.api

_insert_user = UserDto.UserPost
_fetch_user = UserDto.UsersGetAll

@api.route('/')
class Users(Resource):
    @api.expect(_insert_user, validate=True)
    def post(self):
        """Add New User"""
        data = request.json
        return insert_user(data=data)

    @api.marshal_list_with(_fetch_user, envelope='data')
    @api.expect(Const.parser, validate=True)
    def get(self):
        """List Users Details"""
        args = Const.parser.parse_args()
        return fetch_user(data=args)