from pydantic import BaseModel, EmailStr
from datetime import datetime

# Used when registering a new user
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# Used when logging in
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Used for sending user info in responses
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True
