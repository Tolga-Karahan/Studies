from psycopg2 import Timestamp
from datetime import datetime
from pydantic import BaseModel, Field

class Post(BaseModel):
    title: str = Field(...)
    content: str = Field(...)
    published: bool = Field(default=True)

class PostCreate(Post):
    pass

class PostResponse(Post):
    id: int = Field(...)
    created_at: datetime = Field(None) 
    published: bool = Field(...)

    # Added to inform the Pydantic model to read data
    # even it's not a dictionary but a SQLAlchemy model. 
    class Config:
        orm_mode = True