from sqlalchemy.orm import Session
from app.models import User, Post

def get_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, username: str, email: str, password: str):
    new_user = User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_post(db: Session, title: str, content: str, user_id: int):
    new_post = Post(title=title, content=content, user_id=user_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

def get_posts(db: Session):
    return db.query(Post).all()
