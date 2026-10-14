from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

import os
from pathlib import Path

# This creates (or connects to) spendwise.db located in the backend folder
DB_PATH = Path(__file__).resolve().parent / "spendwise.db"
DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False, "timeout": 15}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This function gives each API request its own database session, and closes it when done
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()