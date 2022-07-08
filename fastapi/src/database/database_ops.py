from src.schemas.post_schemas import PostCreate
from src.schemas.user_schemas import UserCreate
from src.database.models import Posts, Users
from sqlalchemy.orm import Session
from src.utils.encrypt import encrypt_password

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

def get_users(db: Session): 
    return db.query(Users).all()

def get_user(user_id: int, db: Session):
    return db.query(Users).filter(Users.id == user_id).first()

def create_user(user_info: UserCreate, db: Session):
    encrypted_password = encrypt_password(user_info.password)
    new_user.password = encrypted_password

    new_user = Users(**user_info.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def delete_user(user_id: int, db: Session):
    user = db.query(Users).filter(Users.id == user_id).first()

    if user == None:
        return False
    
    user.delete(synchronize_session=False)
    db.commit()

    return True

def update_user(user_id, updated_user: UserCreate, db: Session):
    user = db.query(Users).filter(Users.id == user_id).first()

    if user == None:
        return

    user.update(updated_user.dict(), synchronize_session=False)
    db.commit()

    return user