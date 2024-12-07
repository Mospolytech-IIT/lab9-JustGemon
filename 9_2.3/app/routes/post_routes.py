from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(database.get_db)):
    return crud.create_post(db, post.title, post.content, post.user_id)

@router.get("/posts/", response_model= list[schemas.Post])
def read_posts(db: Session = Depends(database.get_db)):
    return crud.get_posts(db)