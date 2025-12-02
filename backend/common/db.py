from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import Settings


Engine = None
SessionLocal = sessionmaker(autocommit=False, autoflush=False)
Base = declarative_base()


def ensure_engine():
    global Engine
    if Engine is None:
        s = Settings()
        if not s.database_url:
            raise RuntimeError("DATABASE_URL not configured")
        Engine = create_engine(s.database_url, pool_pre_ping=True)
        SessionLocal.configure(bind=Engine)
