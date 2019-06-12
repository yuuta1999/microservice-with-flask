# users/app/api/models/roles.py

import datetime

from ..utils.extensions import db

class Roles(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), db.ForeignKey('users.username'), nullable=False)
    roles = db.Column(db.String(128), nullable=False)

    issued_date = db.Column(db.DateTime, nullable=False)



