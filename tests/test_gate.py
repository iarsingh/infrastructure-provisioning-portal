from fastapi.testclient import TestClient
from provportal.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'name': 'payments-dev', 'region': 'us-central1'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'name': 'PROD', 'region': 'us-central1'}).json()
    assert bad["passed"] is False
    assert "bad_name" in bad["failed"]
