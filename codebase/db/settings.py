import logging
import os

from dotenv import load_dotenv
from sqlmodel import create_engine, Session, SQLModel

load_dotenv()


def _create_db_engine(**kwargs):
    """Call to create_engine for db."""
    return create_engine(os.getenv("DB_URI", ""), **kwargs)


_db_engine = _create_db_engine()


def get_db_session() -> Session:
    """Returns a db Session."""
    return Session(_db_engine)


def init_db():
    """Setup DB metadata."""
    SQLModel.metadata.create_all(_db_engine)


def refresh_current_engine():
    """Redo setup DB metadata with changed DB_URI (for tests!)."""
    global _db_engine

    _db_engine = _create_db_engine()
    logging.debug("Setting global engine %s", _db_engine.url)
