
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.models import Base
from app.db.session import get_db

# Setup in-memory SQLite for tests
engine = create_engine("sqlite+pysqlite:///:memory:", future=True)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)
Base.metadata.create_all(bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_create_and_get_user():
    payload = {"email": "test@example.com", "full_name": "Test User"}
    r = client.post("/api/users/", json=payload)
    assert r.status_code == 201, r.text
    data = r.json()
    assert data["email"] == payload["email"]
    assert data["full_name"] == payload["full_name"]

    user_id = data["id"]
    r2 = client.get(f"/api/users/{user_id}")
    assert r2.status_code == 200
    data2 = r2.json()
    assert data2["id"] == user_id
