from app.main.model.user import User
from app.main.model.role import Role
import uuid
from app.main.service.constants import *
from datetime import datetime


# import bson


def insert_user(data):
    try:
        if not data:
            response_object = {
                'status': Const.FAIL,
                'message': 'Role field Required.'
            }
            return response_object, Const.FAILURE_CODE
        data['publicId'] = uuid.uuid4()
        data['createdOn'] = datetime.now()
        # print(data['name']['firstName'])
        data['fullName'] = data['name']['firstName'] + ' ' + data['name']['lastName']
        # print(data)
        data_set = Role.objects.aggregate(
            {'$match': {'publicId': uuid.UUID(data['roleId'])}},
            {"$project": {'_id': 1}}
        )
        role_data = list(data_set)
        print(role_data[0]['_id'])
        data['roleId'] = role_data[0]['_id']
        print(data)
        User(**data).save()
        response_object = {
            'status': Const.SUCCESS,
            'message': Const.USER_INSERT_SUCCESS
        }
        return response_object, Const.SUCCESS_CODE

    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def fetch_user(data):

    lookup_role = {"$lookup": {
        "from": "role",
        "localField": "roleId",
        "foreignField": "_id",
        "as": "roleId"
    }}

    project_data = {"$project": {
            'publicId': 1,
            'username': 1,
            'name': 1,
            'fullName': 1,
            'age': 1,
            'email': 1,
            'phone': 1,
            'roleId': {'role': 1},
            'status': 1
        }}

    conditions = {}

    if 'publicId' in data and data['publicId'] != None:
        conditions['publicId'] = uuid.UUID(data['publicId'])
    conditions['status'] = 'ACTIVE'
    try:
        data_set = User.objects.aggregate(*[
            {"$match": conditions},
            lookup_role,
            project_data
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
