from sqlalchemy.orm import Session

from .models import User as UserModel
from .schemas import UserCreate as UserCreateSchema

def get_users(db: Session):
    return db.query(UserModel).all()

def get_user(db: Session, id: int):
    return db.query(UserModel).filter(UserModel.id == id).first()

def create_user(db: Session, user: UserCreateSchema):
    new_data = UserModel(**user.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data

def delete_user(db: Session, id: int):
    return db.query(UserModel).filter(UserModel.id == id).delete()

def update_user(db: Session, user: UserCreateSchema):
    current_data = db.query(UserModel).filter(UserModel.id == user.id).first()
    new_data = user.dict()
    for k, v in new_data.items():
        setattr(current_data, k, v)
        
    db.commit()
    return new_data