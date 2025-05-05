import base64
import json
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy.orm import Session
from core.database import SessionLocal, Image

class ImageStorageHandler:
    def __init__(self, save_dir="received"):
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)

    def handle(self, payload: dict) -> None:
        db: Session = SessionLocal()
        try:
            satellite = payload.get("satellite", "unknown_sat")
            location = payload.get("location", "unknown_loc")
            location_safe = location.replace(",", "").replace(" ", "_")
            timestamp = payload.get("timestamp", datetime.now(timezone.utc).isoformat())
            ts = timestamp.replace(":", "-").replace("T", "_").split(".")[0]

            filename = f"{satellite}_{location_safe}_{ts}.png"
            filepath = self.save_dir / filename

            image_data = payload["image_data"]
            decoded = base64.b64decode(image_data)

            with open(filepath, "wb") as f:
                f.write(decoded)

            # Save record to database
            db_image = Image(
                filename=filename,
                satellite_name=satellite,
                location=location,
                timestamp=datetime.fromisoformat(timestamp),
                is_shared=True,
                user_id=None  # MQTT uploads aren't linked to a registered user
            )
            db.add(db_image)
            db.commit()

            print(f"Image saved to {filepath} and recorded in DB")

        except Exception as e:
            print(f"Failed to process MQTT payload: {e}")
        finally:
            db.close()
