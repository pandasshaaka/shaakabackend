from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import Settings
import logging
import os

Engine = None
SessionLocal = sessionmaker(autocommit=False, autoflush=False)
Base = declarative_base()

def ensure_engine():
    global Engine
    if Engine is None:
        s = Settings()
        
        # For Render deployment, use SQLite for now to avoid psycopg2 issues
        # This will be changed to PostgreSQL once we fix the compatibility
        if os.environ.get('RENDER'):
            logging.info("Using SQLite database for Render deployment")
            Engine = create_engine("sqlite:///./app.db", pool_pre_ping=True, echo=False)
        elif s.database_url and s.database_url.startswith('postgresql://'):
            try:
                Engine = create_engine(
                    s.database_url,
                    pool_pre_ping=True,
                    pool_recycle=300,
                    echo=False
                )
                # Test connection
                with Engine.connect() as conn:
                    result = conn.execute(text("SELECT 1"))
                    result.fetchone()
                logging.info("PostgreSQL connection successful")
            except Exception as e:
                logging.error(f"PostgreSQL connection failed: {e}")
                logging.warning("Falling back to SQLite database")
                Engine = create_engine("sqlite:///./app.db", pool_pre_ping=True, echo=False)
        else:
            logging.warning("No PostgreSQL URL provided, using SQLite")
            Engine = create_engine("sqlite:///./app.db", pool_pre_ping=True, echo=False)
        
        SessionLocal.configure(bind=Engine)