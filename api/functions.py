from sqlmodel import select, Session

from db.models import User


def get_user_by_email(db: Session, email: str):
    return db.exec(select(User).filter(User.email == email)).first()
