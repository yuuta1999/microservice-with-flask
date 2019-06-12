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

    roles = db.relationship('Roles', backref='users', lazy=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = hash_pwd_with_bcrypt(pwd=password)
        self.email = email

    

