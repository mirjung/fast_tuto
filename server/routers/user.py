from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal, engine, get_db
from db.user import crud, models, schemas

from api.dependency import get_token_header
from api.auth import create_access_token

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get('')
async def index():
    return {'hello': 'world'}

@router.get('/{user_id}', response_model=schemas.User, dependencies=[Depends(get_token_header)])
async def read_user(user_id:int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post('', response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id=user.id)
    if db_user:
        raise HTTPException(status_code=400, detail='Already registered user id')
    user_data = crud.create_user(db=db, user=user)
    return user_data