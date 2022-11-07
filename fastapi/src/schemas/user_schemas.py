from psycopg2 import Timestamp
from datetime import datetime
from pydantic import BaseModel, Field, EmailStr

class User(BaseModel):
    email: EmailStr = Field(...)

class UserCreate(User):
    password: str = Field(...)

class UserResponse(User):
    id: int = Field(...)
    created_at: datetime = Field(...)
    
    # Added to inform the Pydantic model to read data
    # even it's not a dictionary but a SQLAlchemy model. 
    class Config:
        orm_mode = True