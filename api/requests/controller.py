from flask import jsonify, request, Blueprint
from api.requests.service import Requests_service
from api.shared.client_guard import client_guard
from api.shared.operator_guard import operator_guard
from api.shared.utils import RequestStatus
from api.shared.validators import validate_is_enum

requests_bp = Blueprint('Requests', __name__, url_prefix='/requests')

@requests_bp.route('/', methods=['POST'])
@client_guard
def create_request():
    data = request.json
    client_id = request.headers.get('client-id')
    result, status_code = Requests_service.create_request(data, client_id)
    return jsonify(result), status_code.value

@requests_bp.route('/', methods=['GET'])
def get_all_requests():
    result, status_code = Requests_service.get_requests()
    return jsonify(result), status_code.value

@requests_bp.route('/<int:id>', methods=['PUT'])
@client_guard
def update_request(id):
    data = request.json
    result, status_code = Requests_service.update_request(id, data)
    return jsonify(result), status_code.value

@requests_bp.route('/<int:id>', methods=['DELETE'])
@client_guard
def delete_request(id):
    result, status_code = Requests_service.delete_request(id)
    return jsonify(result), status_code.value

@requests_bp.route('/<int:id>/status', methods=['PUT'])
@operator_guard
@validate_is_enum('status', RequestStatus)
def update_request_status(id):
    data = request.json
    operator_id = request.headers.get('operator-id')
    result, status_code = Requests_service.update_request_status(id, data, operator_id)
    return jsonify(result), status_code.value