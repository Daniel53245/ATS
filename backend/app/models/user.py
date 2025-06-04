from sqlalchemy import Column, Interger, String,DateTime, null, true
from sqlalchemy.sql import func
from app.database import Base 

class User(Base):
        __tablename__ = "users"
        
        id = Column(Interger,primary_key=True,index=True)
        email = Column(String,unique=True,index=True,nullable=False)
        hashed_password = Column(String,nullable=False)
        created_at = Column(DateTime(timezone=True),server_default=func.now())
        