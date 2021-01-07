from werkzeug.utils import secure_filename

from app.main.model.user import User
import uuid
from app.main.service.constants import *
from datetime import datetime


def upload_image(data):
    try:
        condition = {}
        # data['profile'] = data['file1'].filename
        if 'publicId' in data and data['publicId'] is not None:
            condition["publicId"] = uuid.UUID(data['publicId'])

            data_set = User.objects.aggregate(*[
                {"$match": condition},
                {"$project": {'publicId': 1, 'profile': 1}}
            ])
            UserData = list(data_set)
            if 'profile' in UserData[0] and UserData[0]['profile'] is not None:
                os.remove(os.path.join(Const.APP_ROOT + '\\files', UserData[0]['profile']))

            file = data['file1']

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                unique_filename = data['publicId'] + '-' + filename
                data['profile'] = unique_filename
                file.save(os.path.join(Const.APP_ROOT + '\\files', unique_filename))
            del data['file1']
            User.objects(publicId=data['publicId']).update(**data)
            response_object = {
                'status': Const.SUCCESS,
                'message': Const.USER_UPLOAD_PROFILE_SUCCESS
            }
            return response_object, Const.SUCCESS_CODE

        else:
            response_object = {
                'status': Const.FAIL,
                'message': "Enter valid public id"
            }
            return response_object, Const.FAILURE_CODE

    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE
