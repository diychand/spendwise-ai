from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# This creates (or connects to) a file called spendwise.db in your project folder
DATABASE_URL = "sqlite:///./spendwise.db"

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