from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from server.db.database import SessionLocal, engine, get_db
from server.db.user import crud, models, schemas

from server.api.dependency import get_token_header
from server.api.auth import create_access_token
from server.api.wrapper import response_wrapper, obj_as_dict

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.post('')
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_data = crud.create_user(db=db, user=user)
    return response_wrapper(**user_data)

@router.get('/{user_id}', dependencies=[Depends(get_token_header)])
async def read_user(user_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND, 
                        detail="User not found"
                    )
    return response_wrapper(**db_user)

@router.put('/{user_id}', dependencies=[Depends(get_token_header)])
async def update_user(user_id: str, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    current_user_data = crud.get_user_by_id(db, id=user_id)
    if current_user_data is None:
        raise HTTPException(
                        status_code=status.HTTP_404_NOT_FOUND, 
                        detail="User not found"
                    )
    updated_user = crud.update_user(db, user=user)
    return response_wrapper(**updated_user)

@router.delete('/{user_id}', dependencies=[Depends(get_token_header)])
async def delete_user(user_id: str, db: Session = Depends(get_db)):
    result = crud.delete_user(db, id=user_id)
    return response_wrapper(**{'success': result})