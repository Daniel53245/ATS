from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_test_user_endpoint():
    response = client.get("/test-user")
    assert response.status_code == 200
    assert response.json() == {"msg": "Backend is connected!"}

def test_docs_endpoint():
    response = client.get("/docs")
    assert response.status_code == 200
    assert "swagger-ui" in response.text

def test_openapi_endpoint():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "openapi" in response.json() 