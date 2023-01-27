from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic.types import UUID4
from sqlmodel import col, select, Session

from api.functions import get_user_by_email
from db.io_schemas import CourseBase, CourseResponse, UserBase, UserResponse
from db.models import Course, User
from db.settings import get_db_session

router = APIRouter()
db_session: Session = Depends(get_db_session)


@router.get("/users", response_model=list[UserResponse])
async def get_users(skip: int = 0, limit: int = 100, db: Session = db_session):
    return db.exec(select(User).offset(skip).limit(limit)).all()


@router.post("/users", response_model=UserResponse, status_code=201)
async def create_new_user(user: UserBase, db: Session = db_session):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Email is already in the system"
        )
    db_user = User(email=user.email, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: UUID4, db: Session = db_session):
    query = select(User).where(User.id_ == user_id)
    db_user = db.execute(query).scalar_one_or_none()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{user_id}/courses", response_model=List[CourseResponse])
async def get_user_courses(user_id: UUID4, db: Session = db_session):
    return db.exec(
        select(Course).filter((col(Course.created_by) == user_id))
    ).all()


@router.get("/courses", response_model=List[CourseResponse])
async def get_courses(db: Session = db_session):
    return db.exec(select(Course)).all()


@router.post("/courses", response_model=CourseResponse)
async def create_new_course(course: CourseBase, db: Session = db_session):
    db_course = Course(
        title=course.title,
        description=course.description,
        created_by=course.created_by,
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course


@router.get("/courses/{course_id}")
async def get_course(course_id: UUID4, db: Session = db_session):
    db_course = db.exec(
        select(Course).filter(col(Course.id_) == course_id)
    ).first()
    if db_course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course
