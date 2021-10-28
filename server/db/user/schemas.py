from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from server.db.post.schemas import Post

class UserBase(BaseModel):
    id: str
    name: str
    email: str

class UserCreate(UserBase):
    password: str
    is_active: bool
    updated_at: Optional[datetime]
    created_at: Optional[datetime]
    
class UserUpdate(UserBase):
    password: str
    is_active: bool
    updated_at: Optional[datetime] = datetime.now()
    
class User(UserBase):
    posts: List[Post] = []
    updated_at: Optional[datetime] = datetime.now()
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True