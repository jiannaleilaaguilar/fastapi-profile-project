import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine, SessionLocal

client = TestClient(app)

@pytest.fixture(autouse=True)
def reset_database():
    # Clear all rows from database before each test run
    db = SessionLocal()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db.close()
    yield
    Base.metadata.drop_all(bind=engine)

def test_read_and_update_profile():
    # 1. Get initial profile
    res = client.get("/api/v1/profile/")
    assert res.status_code == 200
    assert res.json()["username"] == "testuser"

    # 2. Test password change failure (invalid current password)
    res = client.put("/api/v1/profile/password", json={
        "current_password": "WrongPassword123",
        "new_password": "NewSecretPassword123"
    })
    assert res.status_code == 400

    # 3. Test password change success
    res = client.put("/api/v1/profile/password", json={
        "current_password": "OriginalPassword123",
        "new_password": "NewSecretPassword123"
    })
    assert res.status_code == 200
    assert res.json()["message"] == "Password updated successfully"
