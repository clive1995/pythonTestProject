from ..service.role_service import insert_role, fetch_role, delete_role, update_role
# from app.main.util.
from ..util.role_dto import RoleDto
from app.main.service.constants import *
from flask_restplus import Resource
from flask import request

api = RoleDto.api

_insert_role = RoleDto.RolePost
_fetch_role = RoleDto.RoleGetAll
_role_id = RoleDto.RoleId


@api.route('/')
class Role(Resource):
    @api.expect(_insert_role, validate=True)
    def post(self):
        """ Create a new Role
        parameters to be passed:-
        role:- ADMIN/USER/AUDITOR'"""
        data = request.json
        return insert_role(data=data)

    @api.marshal_list_with(_fetch_role, envelope='data')
    @api.expect(Const.parser, validate=True)
    def get(self):
        """ List Roles
        parameter to be Passed:-
        PublicId :- PublicId of user
         if publicId is not provided list of all Roles will be fetched """
        print('fffff')
        data = Const.parser.parse_args()
        print(data)
        return fetch_role(data=data)

    @api.expect(_role_id, validate=True)
    def delete(self):
        """ Delete user """
        data = request.json
        return delete_role(data=data)

    @api.expect(_fetch_role, validate=True)
    def put(self):
        """ Update user details """
        data = request.json
        return update_role(data=data)
