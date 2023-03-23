from datetime import datetime
from config import db 


class TestModel(db.Model):
    __tablename__= 'test'

    id = db.Column(db.Integer, primary_key=True)
    test_date = db.Column(db.DateTime)
    equipment = db.Column(db.String(50))
    configuration_duration = db.Column(db.DateTime)
    configuration_program = db.Column(db.Integer())   
    result_health = db.Column(db.Integer())
    result_capacity = db.Column(db.Integer())
    battery_id = db.Column(db.Integer, db.ForeignKey('battery.id'), nullable=False)
    rel_battery = db.relationship('BatteryModel', back_populates='tests', single_parent=True, cascade="all,delete-orphan")

    def __init__(self, test_date, equipment, configuration_duration, configuration_program, result_health, result_capacity, battery_id):
        self.test_date = test_date
        self.equipment = equipment
        self.configuration_duration = configuration_duration
        self.configuration_program = configuration_program
        self.result_health = result_health
        self.result_capacity = result_capacity
        self.battery_id = battery_id
 