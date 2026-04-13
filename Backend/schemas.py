from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# -------------------------
# USER SCHEMAS
# -------------------------

from pydantic import BaseModel, EmailStr
from typing import Literal

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Literal["user", "operator", "supplier"]

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    role: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class MessageResponse(BaseModel):
    message: str


# -------------------------
# SIMULATION SCHEMAS
# -------------------------

class SimulationCreate(BaseModel):
    title: str
    input_data: str


class SimulationResponse(BaseModel):
    id: int
    title: str
    input_data: str
    result_data: Optional[str] = None
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True

        from typing import Optional


class MatchRequestCreate(BaseModel):
    energy_type: str
    capacity: int
    location: str
    preferences: Optional[str] = None


class MatchRequestResponse(BaseModel):
    id: int
    user_id: int
    province: str
    need_type: str
    message: Optional[str]
    status: str

    class Config:
        from_attributes = True