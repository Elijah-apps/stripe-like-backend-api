# This file is for future use, such as database models.
from pydantic import BaseModel
from typing import Optional

class Payment(BaseModel):
    amount: float
    currency: str
    description: str

class PaymentUpdate(BaseModel):
    amount: Optional[float] = None
    currency: Optional[str] = None
    description: Optional[str] = None

class PaymentMethod(BaseModel):
    type: str
    details: dict

class PaymentMethodUpdate(BaseModel):
    type: Optional[str] = None
    details: Optional[dict] = None

class AccountProfile(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    address: Optional[str] = None

class AccountProfileUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
