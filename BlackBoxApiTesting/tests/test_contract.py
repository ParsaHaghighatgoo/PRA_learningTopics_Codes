import requests
from jsonschema import validate

POST_SCHEMA = {
  "type": "object",
  "required": ["userId","id","title","body"],
  "properties": {
    "userId": {"type": "number"},
    "id":     {"type": "number"},
    "title":  {"type": "string"},
    "body":   {"type": "string"}
  },
  "additionalProperties": True
}

def test_post_contract(base_url):
    r = requests.get(f"{base_url}/posts/1")
    assert r.status_code == 200
    validate(instance=r.json(), schema=POST_SCHEMA)
