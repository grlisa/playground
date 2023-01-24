import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def get_courses():
    return {"courses": []}


@router.post("/courses")
async def create_course():
    return {"courses": []}


@router.get("/courses/{id}")
async def get_course():
    return {"courses": []}


@router.patch("/courses/{id}")
async def update_course():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_course():
    return {"courses": []}
