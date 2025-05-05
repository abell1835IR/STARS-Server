from datetime import datetime
from src.core.database import SessionLocal, Image

def insert_test_images():
    db = SessionLocal()

    sample_data = [
        {
            "filename": "img_2.png",
            "satellite_name": "NOAA-15",
            "location": "Vilnius, Lithuania",
            "timestamp": datetime(2024, 1, 28, 12, 0, 0),
            "is_shared": True,
        },
        {
            "filename": "out_target.png",
            "satellite_name": "NOAA-15",
            "location": "Vilnius, Lithuania",
            "timestamp": datetime(2024, 1, 28, 13, 0, 0),
            "is_shared": True,
        },
        {
            "filename": "test_colorized.png",
            "satellite_name": "NOAA-15",
            "location": "Vilnius, Lithuania",
            "timestamp": datetime(2024, 1, 28, 14, 0, 0),
            "is_shared": True,
        }
    ]

    for entry in sample_data:
        image = Image(
            filename=entry["filename"],
            satellite_name=entry["satellite_name"],
            location=entry["location"],
            timestamp=entry["timestamp"],
            is_shared=entry["is_shared"],
            user_id=None  # or a valid user ID if needed
        )
        db.add(image)

    db.commit()
    db.close()
    print("Sample images added to the database")

if __name__ == "__main__":
    insert_test_images()

