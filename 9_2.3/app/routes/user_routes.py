from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import crud, schemas, database

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user.username, user.email, user.password)

@router.get("/users/", response_model= list[schemas.User])
def read_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db)
