from fastapi import FastAPI
from src.database.database import engine
from src.database.models import Base
from src.routers.posts_router import posts_router
from src.routers.users_router import users_router

api = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

@api.get('/')
async def root():
    return {'api-version':'0.1.0'}

api.include_router(posts_router)
api.include_router(users_router)