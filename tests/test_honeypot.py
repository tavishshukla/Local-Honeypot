from main import app

def test_probe(tmp_path, monkeypatch):
    import main
    monkeypatch.setattr(main, "LOG", tmp_path / "events.jsonl")
    response = app.test_client().get("/admin")
    assert response.status_code == 404
    assert "admin" in (tmp_path / "events.jsonl").read_text()


def test_summary_endpoint(client):
    client.get("/admin")
    response = client.get("/api/summary")
    assert response.status_code == 200
    assert response.get_json()["events"] >= 1
