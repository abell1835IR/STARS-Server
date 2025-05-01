from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from src.core.database import SessionLocal, Image as ImageModel, User as UserModel

router = APIRouter()

def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return """
    <html>
      <head><title>STARS Server</title></head>
      <body>
        <h1>Welcome to STARS Satellite Tracking Server</h1>
        <p><a href="/feed">Public Feed</a> | <a href="/signup">Signup</a> | <a href="/login">Login</a></p>
      </body>
    </html>
    """

@router.get("/feed", response_class=HTMLResponse)
async def public_feed(request: Request, db: SessionLocal = Depends(get_db_session)):
    images = db.query(ImageModel).filter_by(is_shared=True).order_by(ImageModel.timestamp.desc()).all()
    html = "<h1>🌍 Public Satellite Image Feed 🌍</h1><div>"
    for img in images:
        owner = db.query(UserModel).get(img.user_id)
        country = owner.country or "Unknown"
        html += f"<div style='margin-bottom:20px;'>"
        html += f"<h3>From {owner.username} ({country}) at {img.timestamp}</h3>"
        html += f"<img src='/static/uploads/{img.filename}' style='max-width:600px;'/>"
        html += "</div>"
    html += "</div>"
    return HTMLResponse(html)


from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

router = APIRouter()

