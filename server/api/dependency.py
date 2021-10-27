from fastapi import Header, HTTPException, status
from api.auth import valid_access_token

async def get_token_header(authorization: str = Header(...)):
    validation_data = valid_access_token(authorization)
    if not validation_data:
        raise HTTPException(
            status_code=400, detail='Authorization Token invalid'
        )