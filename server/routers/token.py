from typing import Optional

from fastapi import APIRouter, status

from pydantic import BaseModel
from datetime import timedelta

from server.db.database import engine, Base
from server.api import auth, wrapper

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

Base.metadata.create_all(bind=engine)

router = APIRouter()

class TokenData(BaseModel):
    id: str
    name: str
    email: str
    is_active: bool
    

@router.post('')
async def create_access_token(data: TokenData, expires_delta: Optional[timedelta] = None):
    token = auth.create_access_token(data.dict())
    return wrapper.response_wrapper(**token)