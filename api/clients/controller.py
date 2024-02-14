from flask import jsonify, request, Blueprint
from api.clients.service import Clients_service
from api.shared.validators import is_string_length

clients_bp = Blueprint('Clients', __name__, url_prefix='/clients')

@clients_bp.route('/', methods=['POST'])
@is_string_length('first_name', 1, 50)
@is_string_length('last_name', 1, 50)
def create_client():
    data = request.json
    result, status_code = Clients_service.create_client(data)
    return jsonify(result), status_code.value

@clients_bp.route('/', methods=['GET'])
def get_all_clients():
    result, status_code = Clients_service.get_clients()
    return jsonify(result), status_code.value

@clients_bp.route('/<int:id>', methods=['PUT'])
@is_string_length('first_name', 1, 50)
@is_string_length('last_name', 1, 50)
def update_client(id):
    data = request.json
    result, status_code = Clients_service.update_client(id, data)
    return jsonify(result), status_code.value

@clients_bp.route('/<int:id>', methods=['DELETE'])
def delete_client(id):
    result, status_code = Clients_service.delete_client(id)
    return jsonify(result), status_code.value
