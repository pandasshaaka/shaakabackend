"""
Auto-migration for profile photo columns.
This runs automatically when the backend starts to ensure database schema is up to date.
"""

from sqlalchemy import text
import logging

def run_profile_photo_migration(db_session):
    """Automatically add profile photo columns if they don't exist"""
    
    try:
        # Check if columns exist
        check_sql = """
        SELECT column_name 
        FROM information_schema.columns 
        WHERE table_name = 'user_profiles' 
        AND column_name IN ('profile_photo_data', 'profile_photo_mime_type');
        """
        
        result = db_session.execute(text(check_sql))
        existing_columns = {row[0] for row in result.fetchall()}
        
        missing_columns = []
        if 'profile_photo_data' not in existing_columns:
            missing_columns.append('profile_photo_data TEXT')
        if 'profile_photo_mime_type' not in existing_columns:
            missing_columns.append('profile_photo_mime_type VARCHAR(50)')
        
        if missing_columns:
            logging.info(f"Adding missing profile photo columns: {missing_columns}")
            
            # Add missing columns
            for column_def in missing_columns:
                alter_sql = f"ALTER TABLE user_profiles ADD COLUMN IF NOT EXISTS {column_def};"
                db_session.execute(text(alter_sql))
            
            db_session.commit()
            logging.info("✅ Profile photo migration completed successfully!")
        else:
            logging.info("Profile photo columns already exist, skipping migration")
            
    except Exception as e:
        logging.error(f"Profile photo migration failed: {e}")
        db_session.rollback()
        # Don't raise exception - let the app continue