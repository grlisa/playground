import fastapi

router = fastapi.APIRouter()


@router.get("/sections")
async def get_sections():
    return {"sections": []}


@router.post("/sections")
async def create_section():
    return {"sections": []}


@router.get("/sections/{id}")
async def get_section():
    return {"sections": []}


@router.patch("/sections/{id}")
async def update_section():
    return {"sections": []}


@router.delete("/sections/{id}")
async def delete_section():
    return {"sections": []}
