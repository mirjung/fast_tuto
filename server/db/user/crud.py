from sqlalchemy.orm import Session

from .models import User as UserModel
from .schemas import UserCreate as UserCreateSchema

def get_users(db: Session):
    return db.query(UserModel).all()

def get_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.user_id == user_id).first()

def create_user(db: Session, users: UserCreateSchema, user_id: int):
    new_data = UserModel(**users.dict(), user_id=user_id)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def delete_user(db: Session, user_id: int):
    return db.query(UserModel).filter(UserModel.user_id == user_id).delete()

def update_user(db: Session, users: UserCreateSchema, user_id: int):
    current_data = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    new_data = users.dict()
    for k, v in new_data.items():
        setattr(current_data, k, v)
        
    db.commit()
    return new_data