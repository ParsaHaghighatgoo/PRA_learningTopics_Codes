import requests
import pytest

def test_create_read_flow(base_url):
    payload = {"title":"hello","body":"world","userId":1}
    r = requests.post(f"{base_url}/posts", json=payload)
    assert r.status_code in (200,201)
    created = r.json()
    # Simulate read by id if API supports persistence; demo API may echo only
    assert created.get("title") == "hello"

@pytest.mark.parametrize("bad_payload", [
    {}, {"title":123}, {"userId":"x"}, {"title":"", "body":"", "userId":None}
])
def test_bad_inputs(base_url, bad_payload):
    r = requests.post(f"{base_url}/posts", json=bad_payload)
    assert r.status_code in (400,422,500)  # depends on API spec; assert correct one in your real API
