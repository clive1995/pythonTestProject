from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from ..service.upload_service import upload_image
from app.main.service.constants import *
from flask_restplus import Resource
from flask import request, flash
from flask_restplus import reqparse
from flask_restplus import Namespace, fields

api = Namespace('upload', authorizations=Const.authorizations, description='User related operation')

uploadParser = reqparse.RequestParser()
uploadParser.add_argument('publicId', type=str, required=True)
uploadParser.add_argument('file1', location="files", type=FileStorage, required=True)


@api.route('/')
class Upload(Resource):
    target = os.path.join(Const.APP_ROOT, 'files')  # folder path
    if not os.path.isdir(target):
        os.mkdir(target)

    @api.expect(uploadParser, validate=True)
    def put(self):
        """ upload profile Image"""
        data = uploadParser.parse_args()
        return upload_image(data=data)
