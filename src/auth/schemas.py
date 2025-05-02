from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    country: Optional[str] = None 

class UserOut(BaseModel):
    id: int
    username: str
    country: Optional[str] = None

    class Config:
        orm_mode = True