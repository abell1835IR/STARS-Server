from fastapi import APIRouter, Request, Depends, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from core.database import SessionLocal, Image as ImageModel
from . import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        raise HTTPException(status_code=303, detail="Not authenticated")
    user = crud.get_user_by_username(db, username=None) 
    return user

@router.get("/signup", response_class=HTMLResponse)
async def signup_form():
    return """
    <h2>Signup</h2>
    <form action="/signup" method="post">
      <input name="username" placeholder="Username" required><br>
      <input name="password" type="password" placeholder="Password" required><br>
      <input name="country" placeholder="Country (optional)"><br>
      <button>Signup</button>
    </form>"""

@router.post("/signup")
async def signup(
    username: str = Form(...),
    password: str = Form(...),
    country: str = Form(None),
    db: Session = Depends(get_db)
):
    if crud.get_user_by_username(db, username):
        return HTMLResponse("Username taken", status_code=400)
    crud.create_user(db, username, password, country)
    return RedirectResponse("/login", status_code=303)

@router.get("/login", response_class=HTMLResponse)
async def login_form():
    return """
    <h2>Login</h2>
    <form action="/login" method="post">
      <input name="username" placeholder="Username" required><br>
      <input name="password" type="password" placeholder="Password" required><br>
      <button>Login</button>
    </form>"""

@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = crud.authenticate_user(db, username, password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    request.session["user_id"] = user.id
    return RedirectResponse("/dashboard", status_code=303)

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    if not user_id:
        return RedirectResponse("/login", status_code=303)
    images = db.query(ImageModel).filter_by(user_id=user_id).all()
    html = "<h1>Your Gallery</h1>"
    for img in images:
        html += f"<div><h3>{img.satellite_name} at {img.timestamp}</h3>"
        html += f"<img src='/static/uploads/{img.filename}' style='max-width:200px;'/></div>"
    return HTMLResponse(html)

@router.get("/logout")
async def logout(request: Request):
    request.session.clear()
    return RedirectResponse("/", status_code=303)