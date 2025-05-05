from pathlib import Path
from sqlalchemy import (
    create_engine, Column, Integer, String, Boolean, DateTime, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import datetime

DATABASE_URL = "sqlite:///./stars.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    country = Column(String, nullable=True)
    images = relationship("Image", back_populates="owner")

class Image(Base):
    __tablename__ = "images"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    filename = Column(String, nullable=False)
    satellite_name = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    location = Column(String, nullable=True) 
    is_shared = Column(Boolean, default=False)
    owner = relationship("User", back_populates="images")

def init_db():
    Base.metadata.create_all(bind=engine)
