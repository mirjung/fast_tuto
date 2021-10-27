from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from db.post.schemas import Post

class UserBase(BaseModel):
    id: Optional[int]
    email: str
    password: str

class UserCreate(UserBase):
    created_at: Optional[datetime]
    
class User(UserBase):
    is_active: bool
    posts: List[Post] = []
    updated_at: Optional[datetime]
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True