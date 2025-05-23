from fastapi_login import LoginManager

from passlib.context import CryptContext
from slowapi import Limiter
from slowapi.util import get_remote_address

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET = "d47c1400c52aa4405d82e91f81501c498ea79f6c2efadf88"
manager = LoginManager(SECRET, "/login")

limiter = Limiter(key_func=get_remote_address)

