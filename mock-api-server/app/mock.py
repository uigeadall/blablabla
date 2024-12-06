#!/usr/bin/env python3
"""
Mock API for testing
"""
import os

from flask import Flask
from routes.inventory_devices import inventory_devices_bp
from routes.inventory_files import inventory_files_bp


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
    # app.config['SERVER_NAME'] = os.environ['MOCK_HOSTNAME']

    app.register_blueprint(inventory_devices_bp)
    app.register_blueprint(inventory_files_bp)

    return app


mock = create_app()
