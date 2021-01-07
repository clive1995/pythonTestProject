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
                'message': 'field Required.'
            }
            return response_object, Const.FAILURE_CODE
        if data['password'] != data['confirmPassword']:
            response_object = {
                'status': Const.FAIL,
                'message': 'Mismatch password.'
            }
            return response_object, Const.FAILURE_CODE
        data['publicId'] = uuid.uuid4()
        del data['confirmPassword']
        salt = gen_salt()
        data['password'] = hash_password(data['password'], salt)
        data['passwordSalt'] = salt
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
    print(data)
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
        print('test')
        print(details)
        return details
    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def delete_user(data):
    try:
        User.objects(publicId=data['publicId']).delete()
        response_object = {
            'status': Const.SUCCESS,
            'message': Const.USER_DELETE_SUCCESS
        }
        return response_object, Const.SUCCESS_CODE
    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def update_user(data):
    try:
        print('service')
        print(data['publicId'])
        if 'publicId' in data:
            print('yes publicId found')
            if 'name.firstName' in data:
                data['fullName'] = data['name']['firstName'] + ' ' + data['name']['lastName']
            if 'roleId' in data:
                data_set = Role.objects.aggregate(
                    {'$match': {'publicId': uuid.UUID(data['roleId'])}},
                    {"$project": {'_id': 1}}
                )
                role_data = list(data_set)
                print(role_data[0]['_id'])
                data['roleId'] = role_data[0]['_id']
            print('asdasdasda')
            User.objects(publicId=data['publicId']).update(**data)
            response_object = {
                'status': Const.SUCCESS,
                'message': Const.USER_UPDATE_SUCCESS
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


def user_login(data):
    for item in User.objects(email=data['email']):
        verify = verify_password(data['password'], item['password'].encode('utf-8'),  item['passwordSalt'])
        if not verify:
            response_object = {
                'status': Const.FAIL,
                'message': 'Incorrect username or password.'
            }
            return response_object, Const.FAILURE_CODE
        token = generate_active_token(str(item['publicId']), item['roleId']['role'])
        response_object = {
            # 'status': Const.SUCCESS,
            'token': token,
            'publicId': str(item['publicId']),
            'role': item['roleId']['role'],
            'message': 'Successfully logged in.'
        }
        return response_object, Const.SUCCESS_CODE
    response_object = {
        'status': Const.FAIL,
        'message': 'Incorrect username or password.'
    }
    return response_object, Const.FAILURE_CODE
