from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from server.db.database import SessionLocal, engine
from . import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

user_router = APIRouter(
                    prefix='/users',
                    tags=['users']
                )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user_router.get('/{user_id}', response_model=schemas.User)
async def read_user(user_id:int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user_router.post('/{user_id}', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail='Already registered user id')
    return crud.create_user(db=db, user=user)