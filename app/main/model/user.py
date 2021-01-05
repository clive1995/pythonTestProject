from .. import mdb
from app.main.model.role import Role

STATUS = ('ACTIVE', 'INACTIVE')


class Name(mdb.EmbeddedDocument):
    firstName = mdb.StringField()
    lastName = mdb.StringField()


class User(mdb.Document):
    publicId = mdb.UUIDField(binary=True)
    username = mdb.StringField()
    name = mdb.EmbeddedDocumentField(Name)
    fullName = mdb.StringField()
    age = mdb.IntField()
    email = mdb.EmailField()
    phone = mdb.ListField(mdb.StringField())
    roleId = mdb.ReferenceField(Role)
    status = mdb.StringField(choice=STATUS, default='ACTIVE')
    createdOn = mdb.DateField()
