from .. import mdb
import datetime
ROLE = ('ADMIN', 'USER', 'AUDITOR')


class Role(mdb.Document):
    publicId = mdb.UUIDField(binary=True)
    role = mdb.StringField(choices=ROLE)
    createdOn = mdb.DateField()
    updatedOn = mdb.DateTimeField(default=datetime.datetime.utcnow())

