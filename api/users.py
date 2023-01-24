from typing import List, Optional

import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()


users: List[str] = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@router.get("/users", response_model=list[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@router.get("/users/{id}")
async def get_user(_id: int):
    return {"user": users[_id]}
