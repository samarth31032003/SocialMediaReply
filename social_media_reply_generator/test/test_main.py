from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_reply_endpoint():
    payload = {
        "platform": "Twitter",
        "post_text": "Excited about launching our new product!"
    }
    response = client.post("/reply", json=payload)
    assert response.status_code == 200
    json_data = response.json()
    assert "generated_reply" in json_data
    assert len(json_data["generated_reply"]) > 0
