from sqlalchemy.orm import Session
from src.core.database import User, Image
from .security import get_password_hash, verify_password

def create_user(db: Session, username: str, password: str, country: str = None):
    hashed = get_password_hash(password)
    user = User(username=username, hashed_password=hashed, country=country)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user