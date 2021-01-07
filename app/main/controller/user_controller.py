from ..service.user_service import insert_user, fetch_user, delete_user, update_user, user_login
from app.main.util.roles.roles import roles_required
from ..util.user_dto import UserDto
from app.main.service.constants import *
from flask_restplus import Resource
from flask import request
from flask_restplus import reqparse

api = UserDto.api

_insert_user = UserDto.UserPost
_fetch_user = UserDto.UsersGetAll
_delete_user = UserDto.UserDelete
_update_user = UserDto.UserPut
_login_user = UserDto.UserLogin


@api.route('/')
class Users(Resource):
    @api.doc(security='apikey')
    @roles_required('ADMIN')
    @api.expect(_insert_user, validate=True)
    def post(self):
        """Add New User
        parameters to be passed:-
        roleId :- PublicId of role
        status :- ACTIVE/INACTIVE (Default:ACTIVE)"""
        data = request.json
        return insert_user(data=data)

    @api.marshal_list_with(_fetch_user, envelope='data')
    @api.expect(Const.parser, validate=True)
    def get(self):
        """List Users Details
        parameters to be passed:-
        PublicId :- PublicId of User
        if publicId is not provided list of all users will be fetched"""
        args = Const.parser.parse_args()
        return fetch_user(data=args)

    @api.doc(security='apikey')
    @roles_required('ADMIN')
    @api.expect(_delete_user, validate=True)
    def delete(self):
        """ Delete user """
        data = request.json
        return delete_user(data=data)

    @api.expect(_update_user, validate=True)
    def put(self):
        """ Update user details """
        data = request.json
        print(data)
        return update_user(data=data)


@api.route('/<string:publicId>')
class publicIdSimple(Resource):
    @api.marshal_list_with(_fetch_user, envelope='data')
    def get(self, publicId):
        data = {"publicId": publicId}
        print(data)
        return fetch_user(data=data)

@api.route('/login/')
class LoginUser(Resource):
    @api.expect(_login_user, validate=True)
    def post(self):
        """Login for a User"""
        data = request.json
        return user_login(data=data)
