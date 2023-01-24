from fastapi import FastAPI

from api import courses, sections, users

app = FastAPI(
    title="My Fast API",
    description="LMS for managing students and courses",
    version="0.0.1",
    contact={"name": "Lisa", "email": "donotdisturb@email.com"},
)


app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
