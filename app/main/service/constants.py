from flask_restplus import reqparse, fields
# from flask_restplus
from flask_jwt_extended import create_access_token
from app.main import bcrypt
import datetime
import random
import os


class Const():
    authorizations = {
        'apikey': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'X-API-KEY'
        }
    }

    # Message Constants
    SUCCESS = 'SUCCESS'
    FAIL = 'FAIL'
    SUCCESS_CODE = 201
    FAILURE_CODE = 400

    #insert
    ROLE_INSERT_SUCCESS = 'Role added successfully.'
    USER_INSERT_SUCCESS = 'User added successfully.'

    parser = reqparse.RequestParser()
    parser.add_argument('publicId', type=str, required=False)



class DevelopmentConst(Const):
    APP_DEBUG = True
    BASE_URL = "http://127.0.0.1:5000"


const_by_name = dict(
    dev=DevelopmentConst,
    # test=TestingConst,
    # prod=ProductionConst
)
