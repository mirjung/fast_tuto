import secrets
KEY_LENGTH = 32
SECRET_KEY = secrets.token_urlsafe(KEY_LENGTH)
TOKEN_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 30 # minute

