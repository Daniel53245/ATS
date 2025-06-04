# app/routers/auth.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut
from app.models import user as user_model
from app.database import get_db
from app.utils.security import hash_password

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=UserOut)
def register_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # Check if user with same email already exists
    existing_user = (
        db.query(user_model.User)
        .filter(user_model.User.email == user_data.email)
        .first()
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Hash the password and create new user
    hashed_pw = hash_password(user_data.password)
    new_user = user_model.User(email=user_data.email, hashed_password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
