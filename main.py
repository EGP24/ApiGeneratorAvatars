from db.database import database, metadata, engine
from handlers.user import router as user_router
from fastapi import FastAPI
from uvicorn import run


def create_app():
    app = FastAPI()
    app.state.database = database
    app.state.metadata = metadata
    app.state.engine = engine
    app.include_router(user_router)

    @app.on_event("startup")
    async def startup() -> None:
        database_ = app.state.database
        metadata.create_all(engine)
        if not database_.is_connected:
            await database_.connect()

    @app.on_event("shutdown")
    async def shutdown() -> None:
        database_ = app.state.database
        if database_.is_connected:
            await database_.disconnect()

    return app


app = create_app()
if __name__ == '__main__':
    run("main:app", port=8000, host="0.0.0.0", reload=False)