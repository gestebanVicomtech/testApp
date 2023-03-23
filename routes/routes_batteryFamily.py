from models.batteryFamily import BatteryFamilyModel, db
from schemas.batteryFamily_schema import BatteryFamilySchema
from flask import request, jsonify, Blueprint



batteryFamily_route = Blueprint('batteryFamily_blueprint',__name__)
batteryFamily_schema = BatteryFamilySchema()
batteryFamilies_schema = BatteryFamilySchema(many=True)


# Define routes
@batteryFamily_route.route('/batteryfamilies', methods=['GET'])
def get_batteryFamilies():
    batteryFamilies = BatteryFamilyModel.query.all()
    return jsonify(batteryFamilies_schema.dump(batteryFamilies))

@batteryFamily_route.route('/batteryfamilies/<int:id>', methods=['GET'])
def get_batteryFamily(id):
    batteryFamily = BatteryFamilyModel.query.get(id)
    return jsonify(batteryFamily_schema.dump(batteryFamily))

@batteryFamily_route.route('/batteryfamilies', methods=['POST'])
def create_batteryFamily():
    tag = request.json['tag']
    capacity = request.json['capacity']
    type = request.json['type']
    technology = request.json['technology']
    supplier = request.json['supplier']
    batteryFamily = BatteryFamilyModel(tag, capacity, type, technology, supplier)
    db.session.add(batteryFamily)
    db.session.commit()
    return jsonify(batteryFamily_schema.dump(batteryFamily))

@batteryFamily_route.route('/batteryfamilies/<int:id>', methods=['PUT'])
def update_batteryFamily(id):
    batteryFamily = BatteryFamilyModel.query.get(id)
    batteryFamily.tag = request.json['tag']
    batteryFamily.capacity = request.json['capacity']
    batteryFamily.type = request.json['type']
    batteryFamily.technology = request.json['technology']
    batteryFamily.supplier = request.json['supplier']
    db.session.commit()
    return jsonify(batteryFamily_schema.dump(batteryFamily))

@batteryFamily_route.route('/batteryfamilies/<int:id>', methods=['DELETE'])
def delete_batteryFamily(id):
    batteryFamily = BatteryFamilyModel.query.get(id)
    db.session.delete(batteryFamily)
    db.session.commit()
    return jsonify({'message': 'Battery family deleted successfully'})



