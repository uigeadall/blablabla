import pytest
import requests

from Testsing.Test1 import BASE_URL


@pytest.mark.parametrize("url, json_data, expected_status_code", [
    ("/inventory/devices", {"id": "TEST6", "name": "Device 6", "status": "Active"}, 401),
])
def test_post_inventory_devices_unauthorized(url, json_data, expected_status_code):

    response = requests.post(f"{BASE_URL}{url}", json=json_data)
    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}"