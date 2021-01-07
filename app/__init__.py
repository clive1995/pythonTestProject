from flask_restplus import Api
from flask import Blueprint
from .main.controller.user_controller import api as user_ns
from .main.controller.role_controller import api as role_ns
from .main.controller.upload_controller import api as upload_ns
from .main.controller.email_controller import api as email_ns

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint,
          title='TestApi',
          version='1.0',
          description='API web service'
          )


api.add_namespace(user_ns)
api.add_namespace(role_ns)
api.add_namespace(upload_ns)
api.add_namespace(email_ns)

