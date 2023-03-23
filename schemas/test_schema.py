from marshmallow import fields, Schema

class TestSchema(Schema):
    id = fields.Integer(dump_only=True)
    test_date = fields.DateTime(required=True)
    equipment = fields.String(required=True)
    configuration_duration = fields.DateTime(required=True)
    configuration_program = fields.Integer(required=True)
    result_health = fields.Integer(required=True)
    result_capacity = fields.Integer(required=True)
    battery_id = fields.Integer(required=True)