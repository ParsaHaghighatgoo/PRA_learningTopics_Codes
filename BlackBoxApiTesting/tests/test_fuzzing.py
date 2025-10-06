from hypothesis import given, strategies as st
import requests

@given(title=st.text(min_size=0, max_size=100),
       body=st.text(min_size=0, max_size=500))
def test_create_fuzz(base_url, title, body):
    r = requests.post(f"{base_url}/posts", json={"title":title, "body":body, "userId":1})
    assert r.status_code in (200,201,400,422)  # tighten for your API
