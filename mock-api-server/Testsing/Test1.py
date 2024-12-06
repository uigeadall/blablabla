import pytest
import requests
import time

BASE_URL = "http://localhost:8080"


@pytest.mark.parametrize("url, expected_status_code", [
    ("/inventory/devices", 200),
])
def test_get_inventory_devices_status_code_and_time(url, expected_status_code):
    start_time = time.time()
    response = requests.get(f"{BASE_URL}{url}", verify=False)
    end_time = time.time()
    response_time = end_time - start_time

    assert response.status_code == expected_status_code, f"Expected {expected_status_code}, got {response.status_code}"
    assert response_time < 2, "Response time exceeded 2 seconds"
