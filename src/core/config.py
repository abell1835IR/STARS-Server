import yaml
from pathlib import Path

class Config:
    _instance = None 

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.load_config()
        return cls._instance

    def load_config(self):
        config_path = Path(__file__).parent.parent.parent / "config/config.yaml"
        try:
            with open(config_path, 'r') as f:
                self.settings = yaml.safe_load(f)
        except Exception as e:
            raise RuntimeError(f"Error loading config: {e}")

    def get(self, key, default=None):
        keys = key.split('.')
        val = self.settings
        try:
            for k in keys:
                val = val[k]
            return val
        except (KeyError, TypeError):
            return default
