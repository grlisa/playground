from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4


class UserBase(BaseModel):
    email: str
    role: int


class UserResponse(UserBase):
    id_: UUID4
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    created_by: UUID4


class CourseResponse(CourseBase):
    id_: UUID4

    class Config:
        orm_mode = True
