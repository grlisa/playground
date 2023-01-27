import enum
from typing import Optional
from uuid import uuid4

from pydantic import AnyUrl
from pydantic.types import UUID4
from sqlmodel import Field, Relationship, SQLModel

from .mixins import TimeStampMixin

id_field: Optional[UUID4] = Field(
    default_factory=uuid4,
    primary_key=True,
    index=True,
    nullable=False,
)


class Role(enum.IntEnum):
    teacher = 1
    student = 2


class User(SQLModel, TimeStampMixin, table=True):  # type: ignore

    id_: UUID4 = id_field
    email: str = Field(unique=True, index=True, nullable=False)
    role: Role
    is_active: bool = Field(default=False)

    profile: "Profile" = Relationship(
        back_populates="owner"
    )  # , uselist=False
    student_courses: "StudentCourse" = Relationship(back_populates="student")


class Profile(SQLModel, TimeStampMixin, table=True):  # type: ignore

    id_: UUID4 = id_field
    fist_name: str = Field(nullable=False)
    last_name: str = Field(nullable=False)
    bio: str = Field(nullable=True)
    user_id: UUID4 = Field(foreign_key="user.id_", nullable=False)

    owner: User = Relationship(back_populates="profile")


class Course(SQLModel, TimeStampMixin, table=True):  # type: ignore

    id_: UUID4 = id_field
    title: str = Field(nullable=False)
    description: str = Field(nullable=True)
    url: AnyUrl = Field(nullable=True)

    created_by: UUID4 = Field(foreign_key="user.id_", nullable=False)
    student_courses: "StudentCourse" = Relationship(back_populates="course")


class StudentCourse(SQLModel, TimeStampMixin, table=True):  # type: ignore
    """
    Students can be assigned to courses.
    """

    id_: UUID4 = id_field
    student_id: UUID4 = Field(foreign_key="user.id_", nullable=False)
    course_id: UUID4 = Field(foreign_key="course.id_", nullable=False)
    completed: bool = Field(default=False)

    student: User = Relationship(back_populates="student_courses")
    course: Course = Relationship(back_populates="student_courses")
