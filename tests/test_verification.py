from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Testing Area"}

def test_items_crud():
    
    response = client.get("/items")
    assert response.status_code == 200
    assert len(response.json()) == 3

    
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Foo"

    
    new_item = {
        "name": "New Item",
        "price": 15.5,
        "is_offer": True,
        "user_id": 1,
        "category": "C"
    }
    response = client.post("/items", json=new_item)
    assert response.status_code == 201
    item_id = response.json()["id"]
    assert response.json()["name"] == "New Item"

    
    response = client.delete(f"/items/{item_id}")
    assert response.status_code == 204

    
    response = client.get(f"/items/{item_id}")
    assert response.status_code == 404

def test_user_filtering():
    
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "alice"

    
    response = client.get("/users/1/items?category=A")
    assert response.status_code == 200
    items = response.json()
    assert all(i["user_id"] == 1 and i["category"] == "A" for i in items)

def test_upload_schema():
	
    files = {"file": ("test.txt", b"hello content", "text/plain")}
    response = client.post("/upload", files=files)
    assert response.status_code == 200
    assert "filename" in response.json()
    assert "content_type" in response.json()
    assert response.json()["filename"] == "test.txt"
