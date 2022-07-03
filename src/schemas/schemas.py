from psycopg2 import Timestamp
from datetime import datetime
from pydantic import BaseModel, Field

class PostSchema(BaseModel):
    title: str = Field(...)
    content: str = Field(...)
    published: bool = Field(default=True)

class Post(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    content: str = Field(...)
    published: bool = Field(...)
    created_at: datetime = Field(...) 

    class Config:
        orm_mode = True