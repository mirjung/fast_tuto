from sqlalchemy.orm import Session

from server.db.user.models import User as UserModel
from server.db.user.schemas import UserCreate as UserCreateSchema, UserUpdate as UserUpdateSchema

from server.api import wrapper

from datetime import datetime

def get_user_by_id(db: Session, id: int) -> dict:
    user = db.query(UserModel).filter(UserModel.id == id).first()
    return wrapper.obj_as_dict(user)

def get_user_by_email(db: Session, email: str):
    user = db.query(UserModel).filter(UserModel.email == email).first()
    return wrapper.obj_as_dict(user)

def create_user(db: Session, user: UserCreateSchema) -> dict:
    new_data = UserModel(**user.dict())
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return wrapper.obj_as_dict(new_data)

def delete_user(db: Session, id: str) -> bool:
    result = db.query(UserModel).filter(UserModel.id == id).delete()
    db.commit()
    return bool(result)

def update_user(db: Session, user: UserUpdateSchema) -> dict:
    current_user = db.query(UserModel).filter(UserModel.id == user.id).first()
    for k, v in vars(user).items():
        setattr(current_user, k, v)
    current_user.updated_at = datetime.now()
    db.add(current_user)
    db.commit()
    db.refresh(current_user)
    return wrapper.obj_as_dict(current_user)