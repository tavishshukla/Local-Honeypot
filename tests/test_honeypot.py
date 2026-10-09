from main import app

def test_probe(tmp_path, monkeypatch):
    import main
    monkeypatch.setattr(main, "LOG", tmp_path / "events.jsonl")
    response = app.test_client().get("/admin")
    assert response.status_code == 404
    assert "admin" in (tmp_path / "events.jsonl").read_text()
