from pydantic import BaseModel, Field
from typing import Optional

class EmergencyReport(BaseModel):
    message: str = Field(..., example="There is a fire in the kitchen.")

class EmergencyOut(BaseModel):
    id: str
    type: str
    message: str
    timestamp: str
    status: str

class StatusUpdate(BaseModel):
    status: str = Field(..., example="Resolved")

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: str
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str
