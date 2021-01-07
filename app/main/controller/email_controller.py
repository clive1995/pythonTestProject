from flask_restplus import Namespace, Resource
from ..service.email_service import send_mail

from app.main.service.constants import *

api = Namespace('email', authorizations=Const.authorizations, description='User related operation')


@api.route('/')
class Email(Resource):
    @api.expect(Const.parser, validate=True)
    def post(self):
        ''' SEND Email to users '''
        data = Const.parser.parse_args()
        return send_mail(data=data)
