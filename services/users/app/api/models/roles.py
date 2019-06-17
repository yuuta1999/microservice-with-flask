# users/app/api/models/roles.py

import datetime

from ..utils.extensions import db

class Roles(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # don't use ForeignKey anymore.
    username = db.Column(db.String(128), nullable=False)
    roles = db.Column(db.String(128), nullable=False)

    issued_date = db.Column(db.DateTime, nullable=False)

    def __init__(self, data):
        self.username = data.get('username')
        self.roles = data.get('roles')
        self.issued_date = datetime.datetime.utcnow()



