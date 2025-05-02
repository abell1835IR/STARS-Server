import uvicorn
from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from core.config import Config
from core.database import init_db
from core.logger import logger
from auth.routes import router as auth_router
from web.routes import router as web_router

def create_app() -> FastAPI:
    init_db()

    app = FastAPI(
        title="STARS Satellite Tracking Server",
        description="Secure satellite image server with public and private feeds",
        version="1.0.0",
    )

    app.add_middleware(
        SessionMiddleware,
        secret_key=Config().get('authentication.session_key', 'supersecret'),
    )

    app.include_router(auth_router)
    app.include_router(web_router)

    static_dir = Path(__file__).resolve().parent / "static"
    if not static_dir.exists():
        static_dir.mkdir(parents=True, exist_ok=True)
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    logger.info("Application startup complete.")
    return app

def main():
    cfg = Config()
    app = create_app()
    uvicorn.run(
        app,
        host=cfg.get('web.host', '0.0.0.0'),
        port=cfg.get('web.port', 8000),
    )

if __name__ == "__main__":
    main()
