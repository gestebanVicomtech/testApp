from app import ma
from models.battery import BatteryModel

class BatterySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BatteryModel

