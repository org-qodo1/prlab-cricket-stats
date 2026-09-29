from fastapi.testclient import TestClient

from stats.app import app

client = TestClient(app)

SNAPSHOT = {
    "match_id": "m1",
    "runs": 4,
    "wickets": 0,
    "overs": "0.1",
    "last_event": {
        "display": "FOUR",
        "runs_added": 4,
        "wicket_counted": False,
        "legal_delivery": True,
    },
}


def test_record_and_fetch_ledger() -> None:
    recorded = client.post("/matches/m1/snapshots", json=SNAPSHOT)
    assert recorded.status_code == 200
    fetched = client.get("/matches/m1/ledger")
    assert fetched.status_code == 200
    body = fetched.json()
    assert body["runs"] == 4
    assert body["wickets"] == 0
    assert "last_event" not in body
