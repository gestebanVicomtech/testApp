from marshmallow import fields, Schema

class BatterySchema(Schema):
    id = fields.Integer(dump_only=True)
    tag = fields.String(required=True)
    state = fields.Boolean(required=True)
    date_purchase = fields.DateTime(required=True)
    last_analysis = fields.DateTime(required=True)
    health = fields.Integer(required=True)
    life_cycle = fields.Integer(required=True)

