import pytest
import os

def add(a, b):
    return a + b

def test_add():
    assert add(3, 5) == 8

def test_divide():
    def divide(a, b=0):
        return a / b
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)

@pytest.fixture 
def temp_file():
    file_path = "test_temp.txt"
    with open(file_path, "w") as f:
        f.write("Hello, World!")
    yield file_path 
    if os.path.exists(file_path):
        os.remove(file_path)
        
def test_temp_file(temp_file):
    assert os.path.exists(temp_file)
    with open(temp_file, "r") as f:
        assert f.read() == "Hello, World!"
        
def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_get_user_invalid_id(client):
    response = client.get("/api/v1/users/not-an-integer")
    assert response.status_code == 422

users_database = ["user_a", "user_b"]

@pytest.fixture
def admin_user_setup():
    users_database.append("admin_user")
    yield users_database
    if "admin_user" in users_database:
        users_database.remove("admin_user")

def test_admin_user_is_present(admin_user_setup):
    assert "admin_user" in admin_user_setup
    assert len(admin_user_setup) == 3

def test_admin_user_is_not_present_normally():
    assert "admin_user" not in users_database
    assert len(users_database) == 2
