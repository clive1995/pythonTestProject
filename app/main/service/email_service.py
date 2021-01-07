from flask import Flask
from app.main.model.user import User
from app.main.service.constants import *
from flask_mail import Mail, Message

app = Flask(__name__)
# mail = Mail(app)
app.config['MAIL_SERVER'] = Const.MAIL_SERVER
app.config['MAIL_PORT'] = Const.MAIL_PORT
app.config['MAIL_USERNAME'] = Const.MAIL_USERNAME
app.config['MAIL_PASSWORD'] = Const.MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = Const.MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = Const.MAIL_USE_SSL
mail = Mail(app)


def send_mail(data):
    try:
        print(data)
        msg = Message('Hello', sender='gabrielkelly343@gmail.com', recipients=['cox_grace@rediffmail.com'])
        msg.body = "Hello Flask message sent from Flask-Mail"
        mail.send(msg)
        print()
        response_object = {
            'status': Const.SUCCESS,
            'message': 'Mail sent'
        }
        return response_object, Const.SUCCESS_CODE

    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE
