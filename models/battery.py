from datetime import datetime
from config import db 


class BatteryModel(db.Model):
    __tablename__= 'battery'

    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(50), unique=True)
    state = db.Column(db.Boolean())
    date_purchase = db.Column(db.DateTime, default=datetime.utcnow)
    last_analysis = db.Column(db.DateTime)
    health = db.Column(db.Integer())
    life_cycle = db.Column(db.Integer())
    tests = db.relationship('TestModel', uselist = True, back_populates='rel_battery', cascade="all, delete-orphan",single_parent=True)

    def __init__(self, tag, state, health, life_cycle, last_analysis):
        self.tag = tag
        self.state = state
        self.health = health
        self.life_cycle = life_cycle
        self.last_analysis = last_analysis

        