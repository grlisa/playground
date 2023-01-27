from fastapi import FastAPI

from api import routes
from db.settings import init_db


def create_app():
    """Instantiate FastAPI app."""
    app = FastAPI(
        title="My Fast API",
        description="LMS for managing students and courses",
        version="0.0.1",
        contact={"name": "Lisa", "email": "donotdisturb@email.com"},
    )
    app.include_router(routes.router)

    @app.on_event("startup")
    def _on_startup():
        # setup db engine
        init_db()

    return app


application = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:application",
        host="localhost",
        port=8000,
        reload=True,
        http="httptools",
    )
