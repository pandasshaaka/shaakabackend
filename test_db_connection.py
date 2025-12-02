#!/usr/bin/env python3

import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from backend.common.config import Settings

def test_database_connection():
    """Test connection to Neon database and query user data"""
    
    # Get settings
    settings = Settings()
    
    print(f"DATABASE_URL: {settings.database_url}")
    
    if not settings.database_url:
        print("ERROR: DATABASE_URL not configured")
        return
    
    try:
        # Create engine
        engine = create_engine(settings.database_url, pool_pre_ping=True)
        
        # Create session
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()
        
        print("✅ Database connection established successfully!")
        
        # Test query - get all users
        result = session.execute(text("SELECT id, mobile_no, full_name, category, created_at FROM user_profiles ORDER BY created_at DESC"))
        users = result.fetchall()
        
        print(f"\n📊 Found {len(users)} users in database:")
        
        for user in users:
            user_id, mobile_no, full_name, category, created_at = user
            print(f"  - ID: {user_id}")
            print(f"    Mobile: {mobile_no}")
            print(f"    Name: {full_name}")
            print(f"    Category: {category}")
            print(f"    Created: {created_at}")
            print()
        
        # Test specific user
        if users:
            latest_user = users[0]
            print(f"🎯 Latest user: {latest_user[1]} (ID: {latest_user[0]})")
        
        session.close()
        print("✅ Database query completed successfully!")
        
    except Exception as e:
        print(f"❌ Database error: {str(e)}")
        print(f"Error type: {type(e).__name__}")

if __name__ == "__main__":
    test_database_connection()