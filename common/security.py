from passlib.context import CryptContext
from jose import jwt
from .config import Settings


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)


def create_access_token(sub: str, category: str) -> str:
    s = Settings()
    payload = {"sub": sub, "category": category}
    return jwt.encode(payload, s.jwt_secret, algorithm=s.jwt_algorithm)


def decode_token(token: str) -> dict:
    s = Settings()
    return jwt.decode(token, s.jwt_secret, algorithms=[s.jwt_algorithm])
