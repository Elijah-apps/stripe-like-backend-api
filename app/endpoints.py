from fastapi import APIRouter, HTTPException
from app.models import Payment, PaymentUpdate, PaymentMethod, PaymentMethodUpdate, AccountProfile, AccountProfileUpdate
from typing import Dict, List

router = APIRouter()

payments: Dict[str, Dict] = {}
payment_methods: Dict[str, Dict] = {}
account_profiles: Dict[str, Dict] = {}

# Payment Endpoints
@router.post("/payments/{payment_id}", response_model=Payment)
async def create_payment(payment_id: str, payment: Payment):
    if payment_id in payments:
        raise HTTPException(status_code=400, detail="Payment already exists")
    payments[payment_id] = payment.dict()
    return payments[payment_id]

@router.get("/payments/{payment_id}", response_model=Payment)
async def get_payment(payment_id: str):
    if payment_id in payments:
        return payments[payment_id]
    raise HTTPException(status_code=404, detail="Payment not found")

@router.put("/payments/{payment_id}", response_model=Payment)
async def update_payment(payment_id: str, payment: PaymentUpdate):
    if payment_id not in payments:
        raise HTTPException(status_code=404, detail="Payment not found")
    existing_payment = payments[payment_id]
    updated_payment = {**existing_payment, **payment.dict(exclude_unset=True)}
    payments[payment_id] = updated_payment
    return updated_payment

@router.delete("/payments/{payment_id}", response_model=Dict[str, str])
async def delete_payment(payment_id: str):
    if payment_id in payments:
        del payments[payment_id]
        return {"detail": "Payment deleted"}
    raise HTTPException(status_code=404, detail="Payment not found")

# Payment Method Endpoints
@router.post("/payment_methods/{method_id}", response_model=PaymentMethod)
async def create_payment_method(method_id: str, payment_method: PaymentMethod):
    if method_id in payment_methods:
        raise HTTPException(status_code=400, detail="Payment method already exists")
    payment_methods[method_id] = payment_method.dict()
    return payment_methods[method_id]

@router.get("/payment_methods/{method_id}", response_model=PaymentMethod)
async def get_payment_method(method_id: str):
    if method_id in payment_methods:
        return payment_methods[method_id]
    raise HTTPException(status_code=404, detail="Payment method not found")

@router.put("/payment_methods/{method_id}", response_model=PaymentMethod)
async def update_payment_method(method_id: str, payment_method: PaymentMethodUpdate):
    if method_id not in payment_methods:
        raise HTTPException(status_code=404, detail="Payment method not found")
    existing_method = payment_methods[method_id]
    updated_method = {**existing_method, **payment_method.dict(exclude_unset=True)}
    payment_methods[method_id] = updated_method
    return updated_method

@router.delete("/payment_methods/{method_id}", response_model=Dict[str, str])
async def delete_payment_method(method_id: str):
    if method_id in payment_methods:
        del payment_methods[method_id]
        return {"detail": "Payment method deleted"}
    raise HTTPException(status_code=404, detail="Payment method not found")

# Account Profile Endpoints
@router.post("/profiles/{profile_id}", response_model=AccountProfile)
async def create_account_profile(profile_id: str, profile: AccountProfile):
    if profile_id in account_profiles:
        raise HTTPException(status_code=400, detail="Account profile already exists")
    account_profiles[profile_id] = profile.dict()
    return account_profiles[profile_id]

@router.get("/profiles/{profile_id}", response_model=AccountProfile)
async def get_account_profile(profile_id: str):
    if profile_id in account_profiles:
        return account_profiles[profile_id]
    raise HTTPException(status_code=404, detail="Account profile not found")

@router.put("/profiles/{profile_id}", response_model=AccountProfile)
async def update_account_profile(profile_id: str, profile: AccountProfileUpdate):
    if profile_id not in account_profiles:
        raise HTTPException(status_code=404, detail="Account profile not found")
    existing_profile = account_profiles[profile_id]
    updated_profile = {**existing_profile, **profile.dict(exclude_unset=True)}
    account_profiles[profile_id] = updated_profile
    return updated_profile

@router.delete("/profiles/{profile_id}", response_model=Dict[str, str])
async def delete_account_profile(profile_id: str):
    if profile_id in account_profiles:
        del account_profiles[profile_id]
        return {"detail": "Account profile deleted"}
    raise HTTPException(status_code=404, detail="Account profile not found")

# Stripe-like Endpoints (Simplified)
@router.get("/charges", response_model=List[Dict])
async def list_charges():
    # Placeholder for listing charges
    return [{"id": "charge1", "amount": 100.0, "currency": "USD"}]

@router.post("/charges", response_model=Dict[str, str])
async def create_charge(amount: float, currency: str, description: str):
    # Placeholder for creating a charge
    return {"id": "charge1", "amount": amount, "currency": currency, "description": description}

@router.get("/charges/{charge_id}", response_model=Dict[str, str])
async def get_charge(charge_id: str):
    # Placeholder for retrieving a charge
    return {"id": charge_id, "amount": 100.0, "currency": "USD", "description": "Test charge"}
