from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    database_url: str = Field(default="")
    jwt_secret: str = Field(default="change-me")
    jwt_algorithm: str = Field(default="HS256")
    otp_expiry_seconds: int = Field(default=300)

    class Config:
        env_file = "backend/.env"
        env_file_encoding = "utf-8"
