import json
from pathlib import Path

from sqlmodel import select, Session

from codebase.db.models import User
from codebase.db.settings import get_db_session

_PATH = (
    Path(__file__).parent.parent.parent / "alembic" / "data" / "students.json"
)


def get_user_by_email(db: Session, email: str):
    return db.exec(select(User).filter(User.email == email)).first()


def _db_initial_fill(path: Path):
    db_session = get_db_session()
    with open(path) as f:
        students_data = json.loads(f.read())
        for student in students_data:
            db_session.add(User(**student))
        db_session.commit()


if __name__ == "__main__":
    _db_initial_fill(_PATH)
