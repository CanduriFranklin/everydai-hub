import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://admin:admin123@db:5433/everydai_db")

engine = db.create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

try:
    # Drop tables
    session.execute(text("DROP TABLE IF EXISTS app_behavior, calendar, digital_wellness, entertainment, finance, health, meals, productivity, users CASCADE;"))
    session.commit()
    print("Tables dropped successfully.")

    # Check if tables exist
    result = session.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public';"))
    tables = result.fetchall()
    if not tables:
        print("No tables found.")
    else:
        print("Some tables still exist.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    session.close()
    print("Database connection closed.")
