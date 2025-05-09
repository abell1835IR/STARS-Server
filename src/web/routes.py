from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from core.database import SessionLocal, Image as ImageModel, User as UserModel
from pathlib import Path
import os

print("[TEMPLATE DEBUG] Looking in:", Path(__file__).resolve().parent / "templates")

TEMPLATE_DIR = Path(__file__).resolve().parent / "templates"
templates = Jinja2Templates(directory=str(TEMPLATE_DIR))


router = APIRouter()
templates = Jinja2Templates(directory="src/web/templates")

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@router.get("/feed")
def public_feed(request: Request, db: Session = Depends(get_db_session)):
    images = db.query(ImageModel).filter_by(is_shared=True).order_by(ImageModel.timestamp.desc()).all()
    for img in images:
        img.url = f"/uploads/{img.filename}"
    return templates.TemplateResponse("feed.html", {
        "request": request,
        "images": images
    })


    images = []
    for img in image_rows:
        images.append({
            "url": f"/uploads/{img.filename}",
            "satellite": img.satellite,
            "location": img.location,
            "timestamp": img.timestamp.strftime("%Y-%m-%d %H:%M UTC")
        })

    return templates.TemplateResponse("feed.html", {
        "request": request,
        "images": images
    })
