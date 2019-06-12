# users/app/api/schemas/__init__.py

from .users import UserSchema
from .roles import RoleSchema

__all__ = ['user_schema', 'role_schema']

user_schema = UserSchema()
role_schema = RoleSchema()
