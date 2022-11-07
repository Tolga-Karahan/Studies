from http.client import HTTPException
from sqlalchemy.orm import Session
from fastapi import(
    APIRouter,
    Depends,
    Response,
    status
)    
from typing import List

from src.schemas.post_schemas import PostCreate, PostResponse
from src.database.database import get_db
import src.database.database_ops as db_ops

posts_router = APIRouter(prefix='/posts', tags=['Posts'])

@posts_router.get('/get', response_model=List[PostResponse])
async def get_posts(db: Session = Depends(get_db)):
    return db_ops.get_posts(db)  

# id is a path parameter
@posts_router.get('/get/{id}', status_code=status.HTTP_200_OK, response_model=PostResponse)
async def get_post(id: int, db: Session = Depends(get_db)):
    return db_ops.get_post(id, db)

@posts_router.post('/create', status_code=status.HTTP_201_CREATED, response_model=PostResponse)
# async def create_posts(payload: dict = Body(...)):
async def create_posts(new_post: PostCreate, db: Session = Depends(get_db)):
    return db_ops.create_post(new_post, db)

@posts_router.delete('/delete/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int, db: Session = Depends(get_db)):
    result = db_ops.delete_post(id, db)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No post with id:{id}"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@posts_router.put('/update/{id}', status_code=status.HTTP_200_OK, response_model=PostResponse)
async def update_post(id: int, post: PostCreate, db: Session = Depends(get_db)):
    result = db_ops.update_post(id, db)
    
    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No post with id:{id}"
        )

    return post
