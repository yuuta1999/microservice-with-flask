# users/app/api/utils/func.py

import json
import datetime as dt

from .extensions import bcrypt, db

def get_user_by_username(username, db_model):
    """Take username from request and return user object if existed.
    """
    return db_model.query.filter(db_model.username == username).first()

def get_attr_from_obj(obj, exception=None):
    """Get some attributes from user object.
    """
    return dict([(k,v) for k,v in vars(obj).items() if k != exception and not k.startswith('_')])

def get_all_user(db_model):
    """Take username from request and return user object if existed.
    """
    users = db_model.query.all()
    return list([get_attr_from_obj(user, 'password') for user in users])


def get_role(username, role_db):
    """Take username from user and return its role.
    """
    return role_db.query.filter(role_db.username == username).first()

def get_user_by_email(email, db_model):
    """Take an email from request and return user object if existed.
    """
    return db_model.query.filter(db_model.email == email).first()

def hash_pwd_with_bcrypt(pwd):
    """Hash password with Bcrypt algorithm.
    """
    return bcrypt.generate_password_hash(pwd).decode('utf-8')

def verify_bcrypt_pwd(hashed, pwd):
    """Check if hashed password is matched with input password
    """
    return bcrypt.check_password_hash(pw_hash=hashed, password=pwd)

def save_user(user_obj):
    """Save user to database
    """
    db.session.add(user_obj)
    db.session.commit()

def update_user(user_obj, data):
    """Update user to database
    """
    for k,v in data.items():
        if k == 'password':
            v = hash_pwd_with_bcrypt(v)
        setattr(user_obj, k, v)
    user_obj.modified_at = dt.datetime.utcnow()
    db.session.commit()

def delete_user(user_obj):
    """Remove user from database
    """
    db.session.delete(user_obj)
    db.session.commit()

from app.api.models.user import User
class JSONEncoder(json.JSONEncoder):
    """Make some stuff serializable
    """
    def default(self, o):
        if isinstance(o, dt.datetime):
            return str(o)
        if isinstance(o, User):
            return str(o)
