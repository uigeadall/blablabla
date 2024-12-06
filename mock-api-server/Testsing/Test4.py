import requests
import pytest


@pytest.mark.parametrize("url", ["/inventory/devices"])
def test_get_inventory_devices_fail(url):
    response = requests.get(f"http://localhost:8080{url}", verify=False)
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
