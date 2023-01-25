import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_engine(os.getenv("DB_URI", ""), future=True)

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, future=True
)

Base = declarative_base()


def get_db():
    """Creates a database version
    by creating an instance of SessionLocal class"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
