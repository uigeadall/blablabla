import pytest
import requests


@pytest.mark.parametrize("invalid_json_data", ["{id: TEST8, name: 'Device 8'}"])
def test_post_invalid_json_fail(invalid_json_data):
    response = requests.post("http://localhost:8080/inventory/devices", data=invalid_json_data, verify=False)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"