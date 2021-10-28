from typing import List, Optional
from jose import JWTError, jwt
from datetime import datetime, timedelta
from server.api import wrapper
from server.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_TIME, TOKEN_ALGORITHM

from fastapi import status

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    if expires_delta is not None:
        expire = datetime.utcnow() + timedelta(minutes=expires_delta)
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    to_encode = data.copy()
    to_encode.update({'exp': expire})
    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm=TOKEN_ALGORITHM)
    return {'token': encoded_token, 'token_type': 'bearar'}

def valid_access_token(header: str) -> dict or bool:
    _, token = header.split()
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[TOKEN_ALGORITHM])
        response_data = decoded_token
    except JWTError:
        response_data = False
    except Exception as e:
        response_data = False
        
    finally:
        return response_data