from models.battery import BatteryModel, db
from schemas.battery_schema import BatterySchema
from flask import request, jsonify, Blueprint
from config import api 


battery_route = Blueprint('battery_blueprint',__name__)
battery_schema = BatterySchema()
batteries_schema = BatterySchema(many=True)


# Define routes
@battery_route.route('/batteries', methods=['GET'])
def get_batteries():
    batteries = BatteryModel.query.all()
    return jsonify(batteries_schema.dump(batteries))

@battery_route.route('/batteries/<int:id>', methods=['GET'])
def get_battery(id):
    battery = BatteryModel.query.get(id)
    return jsonify(battery_schema.dump(battery))

@battery_route.route('/batteries', methods=['POST'])
def create_battery():
    tag = request.json['tag']
    state = request.json['state']
    health = request.json['health']
    life_cycle = request.json['life_cycle']
    last_analysis = request.json['last_analysis']
    battery = BatteryModel(tag, state, health, life_cycle, last_analysis)
    db.session.add(battery)
    db.session.commit()
    return jsonify(battery_schema.dump(battery))

@battery_route.route('/batteries/<int:id>', methods=['PUT'])
def update_battery(id):
    battery = BatteryModel.query.get(id)
    battery.tag = request.json['tag']
    battery.state = request.json['state']
    battery.health = request.json['health']
    battery.life_cycle = request.json['life_cycle']
    battery.last_analysis = request.json['last_analysis']
    db.session.commit()
    return jsonify(battery_schema.dump(battery))

@battery_route.route('/batteries/<int:id>', methods=['DELETE'])
def delete_battery(id):
    battery = BatteryModel.query.get(id)
    db.session.delete(battery)
    db.session.commit()
    return jsonify({'message': 'Battery deleted successfully'})



