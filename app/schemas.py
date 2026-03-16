from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: str = Field(..., min_length=5, max_length=100)
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6, max_length=100)
    full_name: Optional[str] = ""


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    full_name: str
    avatar_url: str
    balance: float
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    username: Optional[str] = None


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: Optional[int] = None


class BalanceTopUp(BaseModel):
    amount: float = Field(..., gt=0, description="Amount to top up")


class BalanceTransfer(BaseModel):
    receiver_id: int
    amount: float = Field(..., gt=0, description="Amount to transfer")
    description: Optional[str] = ""


class TransactionResponse(BaseModel):
    id: int
    sender_id: Optional[int]
    receiver_id: int
    amount: float
    type: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True


class BalanceResponse(BaseModel):
    balance: float
