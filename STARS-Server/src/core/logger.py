import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from .config import Config

config = Config()

class AppLogger:
    def __init__(self):
        self.logger = logging.getLogger("STARS")
        self._setup_logger()

    def _setup_logger(self):
        if self.logger.handlers:
            return 

        level_str = config.get('logging.level', 'INFO').upper()
        level = getattr(logging, level_str, logging.INFO)
        self.logger.setLevel(level)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

        if config.get('logging.file'):
            log_path = Path(config.get('logging.file'))
            log_path.parent.mkdir(parents=True, exist_ok=True)
            fh = RotatingFileHandler(log_path, maxBytes=5*1024*1024, backupCount=5)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)

    def get_logger(self):
        return self.logger

logger = AppLogger().get_logger()
