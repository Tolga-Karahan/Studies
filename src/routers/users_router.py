from http.client import HTTPException
from sqlalchemy.orm import Session
from fastapi import(
    APIRouter,
    Depends,
    Response,
    status
)    
from typing import List

from src.schemas.user_schemas import UserCreate, UserResponse
from src.database.database import get_db
import src.database.database_ops as db_ops

users_router = APIRouter(prefix="/users")

@users_router.get('/get', response_model=List[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    return db_ops.get_users(db)  

# id is a path parameter
@users_router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
async def get_user(id: int, db: Session = Depends(get_db)):
    return db_ops.get_user(id, db)

@users_router.post('/create', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user_info: UserCreate, db: Session = Depends(get_db)):
    return db_ops.create_user(user_info, db)

@users_router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: int, db: Session = Depends(get_db)):
    result = db_ops.delete_user(id, db)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No post with id:{id}"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@users_router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=UserResponse)
async def update_user(id: int, user_info: UserCreate, db: Session = Depends(get_db)):
    result = db_ops.update_user(id, db)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No post with id:{id}"
        )

    return user_info