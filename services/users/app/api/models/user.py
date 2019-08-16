# users/app/api/models/user.py

import datetime

from .roles import Roles
from ..utils.extensions import db
from ..utils.func import hash_pwd_with_bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)

    is_active = db.Column(db.Boolean(), default=True, nullable=False)
    is_admin = db.Column(db.Boolean(), default=False, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=False)
    modified_at = db.Column(db.DateTime, default=datetime.datetime.utcnow(), nullable=False)

    roles = db.relationship(
        Roles, 
        backref='users', 
        primaryjoin="User.username==Roles.username",
        foreign_keys=[Roles.__table__.c.username],      # Table: Roles, column: username
        passive_deletes=True,                           # Update the table
        cascade='all'                                   # Can drop all the table
    )

    def __init__(self, username, password, email):
        self.username = username
        self.password = hash_pwd_with_bcrypt(pwd=password)
        self.email = email

        self.is_active = True
        self.is_admin = False

        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __str__(self):
        return f"<User {self.username}>"

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active,
            'is_admin': self.is_admin,
        }
