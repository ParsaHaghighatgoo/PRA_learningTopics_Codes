import requests

def test_health_like_endpoint(base_url):
    r = requests.get(f"{base_url}/posts")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
