from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Format: postgresql://[user]:[password]@[host]:[port]/[database_name]
DATABASE_URL = "postgresql://postgres:1234@localhost:5432/feedback_db"

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for your database models
Base = declarative_base()


# Dependency to get the DB session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
