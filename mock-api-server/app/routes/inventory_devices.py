"""
Inventory devices routes
"""

from flask import Blueprint, jsonify, request
from .common_helper import read_json_file


inventory_devices_bp = Blueprint('inventory_devices', __name__)

INVENTORY_DEVICES_URL = '/inventory/devices'
DEFAULT_INVENTORY_DEVICES_RESPONSE_FILE = '/opt/project/responses/inventory_devices.json'
default_inventory_devices_response = read_json_file(DEFAULT_INVENTORY_DEVICES_RESPONSE_FILE)

GUID_GET_URL = '/guids'
GUID_ADD_URL = '/<path:guid>/add'
DEFAULT_GUIDS_RESPONSE_FILE = '/opt/project/responses/guids.json'
default_guids_response = read_json_file(DEFAULT_GUIDS_RESPONSE_FILE)


@inventory_devices_bp.route(INVENTORY_DEVICES_URL, methods=['GET'])
def get_inventory_appliances():
    return (jsonify(default_inventory_devices_response['body']),
            default_inventory_devices_response['status_code'])


@inventory_devices_bp.route(INVENTORY_DEVICES_URL, methods=['PUT'])
def update_response_inventory_appliances():
    data = request.get_json()
    default_inventory_devices_response['body'] = data['body']
    default_inventory_devices_response['status_code'] = data['status_code']
    return jsonify({'new_body': default_inventory_devices_response['body'],
                    'new_status_code': default_inventory_devices_response['status_code']}), 200


@inventory_devices_bp.route(GUID_ADD_URL, methods=['POST'])
def post_guid_add(guid):
    default_guids_response['body']['guids'].append(guid)
    return (jsonify(default_guids_response['body']),
            default_guids_response['status_code'])


@inventory_devices_bp.route(GUID_GET_URL, methods=['GET'])
def get_guids():
    return (jsonify(default_guids_response['body']),
            default_guids_response['status_code'])


@inventory_devices_bp.route(GUID_GET_URL, methods=['PUT'])
def update_guids():
    data = request.get_json()
    default_guids_response['body'] = data['body']
    default_guids_response['status_code'] = data['status_code']
    return jsonify({'new_body': default_guids_response['body'],
                    'new_status_code': default_guids_response['status_code']}), 200
