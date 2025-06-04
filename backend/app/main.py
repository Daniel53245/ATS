from fastapi import FastAPI
from app.schemas.user import UserOut
from datetime import datetime

app = FastAPI()

@app.get("/test-user", response_model=UserOut)
def test_user():
    return {
        "id": 1,
        "email": "test@example.com",
        "created_at": datetime.utcnow()
    }

