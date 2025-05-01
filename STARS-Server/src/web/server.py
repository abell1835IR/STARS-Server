from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.core.logger import logger
from src.core.config import Config

class WebServer:
    def __init__(self):
        self.config = Config()
        self.app = FastAPI(title="STARS Server")
        self.templates = Jinja2Templates(directory="templates")
        self._setup_routes()
        self._mount_static()
        logger.info("Web server initialized")

    def _setup_routes(self):
        @self.app.get("/")
        async def root():
            return {"message": "Server operational"}

    def _mount_static(self):
        self.app.mount("/static", StaticFiles(directory="static"), name="static")

    def get_app(self):
        return self.app