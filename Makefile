.PHONY: run install build clean

ifeq ($(OS),Windows_NT)
PYTHON = python
PIP = pip
else
PYTHON = python3
PIP = pip3
endif

install: requirements.txt
	$(PIP) install -r requirements.txt

# FastAPI run command
run:
	$(PYTHON) -m uvicorn app.main:app --reload

build: 
	docker build -t fastapi-learning .

docker-run:
	docker run -p 8000:8000 fastapi-learning

test:
	$(PYTHON) -m pytest tests/test.py -v

clean:
ifeq ($(OS),Windows_NT)
	if exist "build" rd /s /q build
	if exist "dist" rd /s /q dist
	if exist "fastapi_learning.egg-info" rd /s /q fastapi_learning.egg-info
else
	rm -rf build dist fastapi_learning.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} +
endif