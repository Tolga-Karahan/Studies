from src.schemas.schemas import PostCreate
from src.database.models import Posts
from sqlalchemy.orm import Session

def get_posts(db: Session): 
    return db.query(Posts).all()

def get_post(post_id: int, db: Session):
    return db.query(Posts).filter(Posts.id == post_id).first()

def create_post(post: PostCreate, db: Session):
    new_post = Posts(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post

def delete_post(post_id: int, db: Session):
    post = db.query(Posts).filter(Posts.id == post_id).first()

    if post == None:
        return False
    
    post.delete(synchronize_session=False)
    db.commit()

    return True

def update_post(post_id, updated_post: PostCreate, db: Session):
    post = db.query(Posts).filter(Posts.id == post_id).first()

    if post == None:
        return

    post.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post
