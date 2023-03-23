from config import db


class BatteryFamilyModel(db.Model):
    __tablename__= 'batteryFamily'
    tag = db.Column(db.String(50), primary_key=True)
    capacity = db.Column(db.Integer())
    type = db.Column(db.Boolean())
    technology = db.Column(db.String(50))
    supplier = db.Column(db.String(50))

    def __init__(self, tag, capacity, type, technology, supplier):
        self.tag = tag
        self.capacity = capacity
        self.type = type
        self.technology = technology
        self.supplier = supplier