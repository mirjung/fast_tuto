from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from server.db.database import Base

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey('users.id'))
    updated_at = Column(DateTime, default=datetime.now)
    created_at = Column(DateTime, default=datetime.now)