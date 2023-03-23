from marshmallow import fields, Schema

class BatteryFamilySchema(Schema):
    tag = fields.String(required=True)
    capacity = fields.Integer(required=True)
    type = fields.Boolean(required=True)
    technology = fields.String(required=True)
    supplier = fields.String(required=True)
    
