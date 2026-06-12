import pytest
from fastapi.testclient import TestClient
from main import app

#client = TestClient(app)

def test_create_task(client):
    response = client.post("/tasks/", json={"title": "test_task", "description": "testing"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "test_task"
    assert data["description"] == "testing"

def test_read_task(client):
    response = client.get(f"/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_task(client):
    create = client.post("/tasks/", json={"title": "old task", "description": "test_description"})
    task_id = create.json()["id"]

    response = client.put(f"/tasks/{task_id}", json={"title": "updated_task", "description": "test_updated"})
    assert response.status_code == 200
    assert response.json()["title"] == "updated_task"

def test_delete_task(client):
    create = client.post("/tasks/", json={"title": "task to delete", "description": "delete description"})
    task_id = create.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    get = client.get(f"/tasks/{task_id}")
    assert get.status_code == 404


