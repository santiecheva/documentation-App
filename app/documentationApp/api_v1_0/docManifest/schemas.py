from marshmallow import fields

from app.ext import ma

class ManifestSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
