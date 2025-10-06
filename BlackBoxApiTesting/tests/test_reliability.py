import requests, time

def test_timeout_and_retry(base_url):
    for attempt in range(3):
        try:
            r = requests.get(f"{base_url}/posts", timeout=2)
            assert r.status_code == 200
            return
        except requests.Timeout:
            if attempt == 2: raise
            time.sleep(0.5 * (attempt+1))
