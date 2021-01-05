from ..service.role_service import insert_role
# from app.main.util.
from ..util.role_dto import RoleDto
from app.main.service.constants import *
from flask_restplus import Resource
from flask import request

api = RoleDto.api

_insert_role = RoleDto.RolePost


@api.route('/')
class Role(Resource):
    @api.expect(_insert_role, validate=True)
    def post(self):
        """ Create a new Role"""
        data = request.json
        return insert_role(data=data)

