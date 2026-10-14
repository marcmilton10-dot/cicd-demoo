from app import app

client = app.test_client()


def test_home_page():
    r = client.get("/")
    assert r.status_code == 200
    assert b"Hello" in r.data


def test_health():
    r = client.get("/health")
    assert r.get_json()["status"] == "ok"


def test_add():
    r = client.get("/add/2/3")
    assert r.get_json()["result"] == 5
