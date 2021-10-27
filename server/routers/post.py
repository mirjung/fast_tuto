from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import SessionLocal, engine, get_db
from db.post import crud as post_crud, models, schemas
from db.user import crud as user_crud

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get('')
async def index():
    return {'hello': 'world'}

@router.get('/{post_id}', response_model=schemas.Post)
async def read_post(post_id:int, db: Session = Depends(get_db)):
    db_item = post_crud.get_post(db, id=post_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_item

@router.post('', response_model=schemas.Post)
async def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, id=post.author_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return post_crud.create_post(db=db, posts=post)