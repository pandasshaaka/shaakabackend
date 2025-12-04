#!/usr/bin/env python3
"""
Database migration script to add profile photo columns to user_profiles table.
Run this to add the new columns for storing profile pictures in Neon PostgreSQL.
"""

import os
import sys
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Add the backend directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from common.config import Settings

def migrate_database():
    """Add profile photo columns to user_profiles table"""
    
    settings = Settings()
    database_url = settings.database_url
    
    print(f"Connecting to database: {database_url}")
    
    try:
        # Create engine and connect
        engine = create_engine(database_url)
        
        # Create session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # SQL to add new columns
        migration_sql = """
        ALTER TABLE user_profiles 
        ADD COLUMN IF NOT EXISTS profile_photo_data TEXT,
        ADD COLUMN IF NOT EXISTS profile_photo_mime_type VARCHAR(50);
        """
        
        print("Executing migration...")
        session.execute(text(migration_sql))
        session.commit()
        
        print("✅ Migration completed successfully!")
        print("Added columns: profile_photo_data, profile_photo_mime_type")
        
        # Verify the changes
        verify_sql = """
        SELECT column_name, data_type, character_maximum_length
        FROM information_schema.columns 
        WHERE table_name = 'user_profiles' 
        AND column_name IN ('profile_photo_data', 'profile_photo_mime_type');
        """
        
        result = session.execute(text(verify_sql))
        columns = result.fetchall()
        
        print("\n📊 Verified columns:")
        for column in columns:
            print(f"  - {column.column_name}: {column.data_type} ({column.character_maximum_length or 'N/A'})")
        
        session.close()
        
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        if 'session' in locals():
            session.rollback()
            session.close()
        sys.exit(1)

if __name__ == "__main__":
    migrate_database()