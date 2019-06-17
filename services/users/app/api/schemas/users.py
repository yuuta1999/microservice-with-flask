# users/app/api/schemas/users.py

from marshmallow import Schema, fields, validate

from .roles import RoleSchema

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(
        required=True, 
        validate=[validate.Length(min=1, error='Cannot be empty string')]
    )
    password = fields.Str(
        required=True, 
        load_only=True,
        validate=[validate.Length(min=1, error='Cannot be empty string')]
    )
    email = fields.Email(required=True)
    is_active = fields.Bool()
    is_admin = fields.Bool()

    created_at = fields.DateTime()
    modified_at = fields.DateTime()

    roles = fields.Nested(RoleSchema, only=("id", "username"), many=True)

