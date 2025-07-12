#!/usr/bin/env python3
"""
Quick setup script to initialize the SQLite database with sample data.
Run this once to get started with your admin system.
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, db
from create_admin import create_admin_user, create_sample_services, create_sample_industries

def setup_database():
    """Initialize the database and create sample data."""
    with app.app_context():
        print("🗄️  Setting up SQLite database...")
        
        # Create all tables
        db.create_all()
        print("✅ Database tables created")
        
        # Create admin user and sample data
        print("👤 Creating admin user...")
        create_admin_user()
        
        print("🛠️  Creating sample services...")
        create_sample_services()
        
        print("🏭 Creating sample industries...")
        create_sample_industries()
        
        print("\n🎉 Setup complete!")
        print("\n📋 Next steps:")
        print("1. Run: python main.py")
        print("2. Open: http://localhost:5000")
        print("3. Hover over navbar → click admin button")
        print("4. Login: admin / admin123")
        print("5. ⚠️  CHANGE DEFAULT PASSWORD!")
        
        print(f"\n💾 Database file: {os.path.abspath('optimum_value.db')}")

if __name__ == '__main__':
    setup_database()