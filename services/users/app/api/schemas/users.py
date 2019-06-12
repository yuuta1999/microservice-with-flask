# users/app/api/schemas/users.py

from marshmallow import Schema, fields

from .roles import RoleSchema

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    email = fields.Email(required=True)
    is_active = fields.Bool()
    is_admin = fields.Bool()

    created_at = fields.DateTime()
    modified_at = fields.DateTime()

    roles = fields.Nested(RoleSchema, only=("id", "username"), many=True)

