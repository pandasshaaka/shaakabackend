from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    database_url: str = Field(default="", alias="DATABASE_URL")
    jwt_secret: str = Field(default="change-me", alias="JWT_SECRET")
    jwt_algorithm: str = Field(default="HS256", alias="JWT_ALGORITHM")
    otp_expiry_seconds: int = Field(default=300, alias="OTP_EXPIRY_SECONDS")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
