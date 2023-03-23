from models.test import TestModel, db
from schemas.test_schema import TestSchema
from flask import request, jsonify, Blueprint



test_route = Blueprint('test_blueprint',__name__)
test_schema = TestSchema()
tests_schema = TestSchema(many=True)


# Define routes
@test_route.route('/batteries/<battery_id>/tests', methods=['GET'])
def get_tests(battery_id):
    tests = TestModel.query.filter_by(battery_id=battery_id).all()
    return jsonify(tests_schema.dump(tests))

@test_route.route('/batteries/<battery_id>/tests/<test_id>', methods=['GET'])
def get_test(battery_id, test_id):
    test = TestModel.query.filter_by(id=test_id, battery_id=battery_id).first()
    return jsonify(test_schema.dump(test))

@test_route.route('/batteries/<battery_id>/tests', methods=['POST'])
def create_test(battery_id):
    test_date = request.json['test_date']
    equipment = request.json['equipment']
    configuration_duration = request.json['configuration_duration']
    configuration_program = request.json['configuration_program']
    result_health = request.json.get['result_health']
    result_capacity = request.json.get['result_capacity']
    test = TestModel(test_date, equipment, configuration_duration, configuration_program, result_health, result_capacity, battery_id=battery_id)
    db.session.add(test)
    db.session.commit()
    return jsonify(test_schema.dump(test))

@test_route.route('/batteries/<battery_id>/tests/<test_id>', methods=['PUT'])
def update_test(battery_id, test_id):
    test = TestModel.query.filter_by(id=test_id, battery_id=battery_id).first()
    test.test_date = request.json['test_date']
    test.equipment = request.json['equipment']
    test.configuration_duration = request.json['configuration_duration']
    test.configuration_program = request.json['configuration_program']
    test.result_health = request.json['result_health']
    test.result_capacity = request.json['result_capacity']
    db.session.commit()
    return jsonify(test_schema.dump(test))

@test_route.route('/batteries/<battery_id>/tests/<test_id>', methods=['DELETE'])
def delete_test(battery_id, test_id):
    test = TestModel.query.filter_by(id=test_id, battery_id=battery_id).first()
    db.session.delete(test)
    db.session.commit()
    return jsonify({'message': 'Test deleted successfully'})