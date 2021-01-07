from flask_restplus import reqparse, fields
# from flask_restplus
from flask_jwt_extended import create_access_token
from app.main import bcrypt
import datetime
import random
import os


def gen_salt():
    salt = str(os.urandom(random.randint(14, 18))).lstrip('b')
    return salt


def hash_password(password_string, salt):
    hash_pwd = bcrypt.generate_password_hash(salt + password_string)
    return hash_pwd


def verify_password(provided, password_hash, salt):
    return bcrypt.check_password_hash(password_hash, salt + provided)


def generate_active_token(public_id, role):
    try:
        identity = {
            'publicId': public_id,
            'role': role
        }
        access_token = create_access_token(expires_delta=False, identity=identity)
        return access_token
    except Exception as e:
        return e


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

    # insert
    ROLE_INSERT_SUCCESS = 'Role added successfully.'
    ROLE_UPDATE_SUCCESS = 'Role updated Successfully'
    ROLE_DELETE_SUCCESS = 'Role deleted  successfully'
    USER_INSERT_SUCCESS = 'User added successfully.'
    USER_UPLOAD_PROFILE_SUCCESS = 'Profile uploaded successfully'
    USER_DELETE_SUCCESS = "User deleted  successfully"
    USER_UPDATE_SUCCESS = "User updated  successfully"

    parser = reqparse.RequestParser()
    parser.add_argument('publicId', type=str, required=False)

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    APP_ROOT = os.path.dirname(os.path.abspath(__name__))

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = 'gabrielkelly343@gmail.com'
    MAIL_PASSWORD = 'Gay@0912'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True


class DevelopmentConst(Const):
    APP_DEBUG = True
    BASE_URL = "http://127.0.0.1:5000"


const_by_name = dict(
    dev=DevelopmentConst,
    # test=TestingConst,
    # prod=ProductionConst
)


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in Const.ALLOWED_EXTENSIONS
