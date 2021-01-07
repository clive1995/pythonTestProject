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


def fetch_role(data):
    print('ghhhhhiiii')
    condition = {}
    if 'publicId' in data and data['publicId'] is not None:
        condition['publicId'] = uuid.UUID(data['publicId'])

    try:

        data_set = Role.objects.aggregate(*[
            {"$match": condition},
            {"$project": {'publicId': 1, 'role': 1}}
        ])
        details = list(data_set)
        print(details)
        return details
    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def delete_role(data):
    try:
        Role.objects(publicId=data['publicId']).delete()
        response_object = {
            'status': Const.SUCCESS,
            'message': Const.ROLE_DELETE_SUCCESS
        }
        return response_object, Const.SUCCESS_CODE
    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def update_role(data):
    try:
        if data['publicId']:
            Role.objects(publicId=data['publicId']).update(**data)
            response_object = {
                'status': Const.SUCCESS,
                'message': Const.ROLE_UPDATE_SUCCESS
            }
            return response_object, Const.SUCCESS_CODE
        else:
            response_object = {
                'status': Const.FAIL,
                'message': "publicId is required"
            }
            return response_object, Const.FAILURE_CODE

    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE
