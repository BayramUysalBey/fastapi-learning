import pytest
import os
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app


def test_main_home(client):
	response = client.get("/")
	assert response.status_code == 200
	assert response.json() == {
		"message": "Welcome to the Dementia Tracker V1 API"
	}

def add(a, b):
	return a + b
def test_add():
	assert add(3,5) == 8


def divide(a, b=0):
	return a / b 
def test_divide():
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
        

@app.get("/")
async def main():
    return {"message": "Hello World"}

def test_main(client):
      response = client.get("/")
      assert response.status_code == 200
      assert response.json() == {"message": "Hello World"}

def test_get_user_invalid_id(client):
    response = client.get("/users/not-an-integer")
    assert response.status_code == 422
    assert "Input should be a valid integer" in response.json()["detail"][0]["msg"]



users_database = ["user_a", "user_b"]

@pytest.fixture
def admin_user_setup():
    users_database.append("admin_user")
    print(f"Added Admin User. Current users: {users_database}")
    yield users_database
    if "admin_user" in users_database:
        users_database.remove("admin_user")
    print(f"Removed Admin User. Current users: {users_database}")

def test_admin_user_is_present(admin_user_setup):
    assert "admin_user" in admin_user_setup
    assert len(admin_user_setup) == 3 # admin_user_setup is a list of users

def test_admin_user_is_not_present_normally():
    assert "admin_user" not in users_database
    assert len(users_database) == 2 # users_database is a list of users



@pytest.fixture(scope="session", autouse=True) # autouse=True means this fixture will be used by default for all tests
def session_fixture():
    print("Starting Test Suite")
    yield
    print("Finished Test Suite")

@pytest.fixture(scope="function", autouse=True) 

def function_fixture():
    print("Starting individual Test")

def test_scope_demo(function_fixture):
    print("Running the actual test code")
    assert True
# pytest -s test.py  # -s flag is used to print the output of the print statements
