"""
Inventory files routes
"""
import os

from flask import Blueprint, send_file, request

inventory_files_bp = Blueprint('inventory_files', __name__)

UPLOAD_FOLDER = '/opt/project/upload'
FILE_ADD_URL = '/file/add'

ROOT_CA_URL = '/mock_certs/root_ca'
ROOT_CA_PATH = '/root/ca/rsa/certs/ca.cert.pem'

INTERMEDIATE_CA_URL = '/mock_certs/intermediate_ca'
INTERMEDIATE_CA_PATH = '/root/ca/rsa/intermediate/certs/intermediate.cert.pem'


@inventory_files_bp.route(ROOT_CA_URL, methods=['GET'])
def get_root_ca_cert():
    return send_file(ROOT_CA_PATH, as_attachment=True)


@inventory_files_bp.route(INTERMEDIATE_CA_URL, methods=['GET'])
def get_intermediate_ca_cert():
    return send_file(INTERMEDIATE_CA_PATH, as_attachment=True)


@inventory_files_bp.route(FILE_ADD_URL, methods=['POST'])
def post_image_add():
    if 'file' not in request.files:
        return "No file part in the request", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    return f"File uploaded successfully to {filepath}", 200
