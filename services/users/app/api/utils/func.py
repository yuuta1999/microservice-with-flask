# users/app/api/utils/func.py

import datetime as dt

from .extensions import bcrypt, db

def get_user_by_username(username, db_model):
    """Take username from request and return user object.
    """
    return db_model.query.filter(db_model.username == username).first()

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
            user_obj.password = hash_pwd_with_bcrypt(v)
        setattr(user_obj, k, v)
    user_obj.modified_at = dt.datetime.utcnow()
    db.session.commit()

def delete_user(user_obj):
    """Remove user from database
    """
    db.session.delete(user_obj)
    db.session.commit()


