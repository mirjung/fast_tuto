from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

class PostBase(BaseModel):
    id: Optional[int]
    title: str
    content: str
    
class PostCreate(PostBase):
    author_id: int
    created_at: Optional[datetime]

class Post(PostBase):
    updated_at: Optional[datetime]
    
    class Config:
        orm_mode = True
        # arbitrary_types_allowed = True