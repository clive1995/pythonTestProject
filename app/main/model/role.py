from .. import mdb

ROLE = ('ADMIN', 'USER', 'AUDITOR')


class Role(mdb.Document):
    publicId = mdb.UUIDField(binary=True)
    role = mdb.StringField(choices=ROLE)
    createdOn = mdb.DateField()

