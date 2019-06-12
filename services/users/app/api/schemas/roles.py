# users/app/api/schemas/roles.py

from marshmallow import Schema, fields

class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    role = fields.Str(required=True, load_only=True)

    issued_date = fields.DateTime()
    
