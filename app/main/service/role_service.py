from app.main.model.role import Role
import uuid
from app.main.service.constants import *
from datetime import datetime


def insert_role(data):
    try:
        if not data['role']:
            response_object = {
                'status': Const.FAIL,
                'message': 'Role field Required.'
            }
            return response_object, Const.FAILURE_CODE
        data['publicId'] = uuid.uuid4()
        data['createdOn'] = datetime.now()
        # print(data)
        Role(**data).save()
        response_object = {
            'status': Const.SUCCESS,
            'message': Const.ROLE_INSERT_SUCCESS
        }
        return response_object, Const.SUCCESS_CODE

    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE
