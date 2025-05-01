import paho.mqtt.client as mqtt
from ..core.logger import logger
from ..core.config import Config

class MQTTClient:
    def __init__(self):
        self.config = Config()
        self.client = mqtt.Client()
        self.subscribers = []
        self._setup_callbacks()
        self.db = Database()

    def _setup_callbacks(self):
        self.client.on_connect = self._on_connect
        self.client.on_message = self._on_message

    def add_subscriber(self, callback):
        self.subscribers.append(callback)

    def _process_message(self, payload):
        image_data = self._decode_payload(payload)
        if self.config.get('database.enabled'):
            self._store_image(image_data)
        return image_data

    @abstractmethod
    def _decode_payload(self, payload):
        pass

    def _store_image(self, image_data):
        session = self.db.get_session()
        if session:
            new_image = SatelliteImage(
                timestamp=datetime.now(),
                image_path=image_data['path'],
                user_id=image_data.get('user_id')
            )
            session.add(new_image)
            session.commit()
            session.close()