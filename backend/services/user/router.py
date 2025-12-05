from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from common.db import SessionLocal, ensure_engine
from common.models import UserProfile
from common.security import decode_token
from pydantic import BaseModel
from typing import Optional

router = APIRouter()
security = HTTPBearer()

class ProfileUpdateRequest(BaseModel):
    full_name: str
    mobile_no: str
    gender: str
    address_line: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    pincode: Optional[str] = None
    profile_photo_data: Optional[str] = None
    profile_photo_mime_type: Optional[str] = None


def get_db():
    ensure_engine()
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/me")
def me(creds: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)):
    data = decode_token(creds.credentials)
    uid = data.get("sub")
    if not uid:
        raise HTTPException(status_code=401, detail="invalid_token")
    obj = db.query(UserProfile).filter(UserProfile.id == uid).first()
    if not obj:
        raise HTTPException(status_code=404, detail="not_found")
    return {
        "id": str(obj.id),
        "full_name": obj.full_name,
        "mobile_no": obj.mobile_no,
        "gender": obj.gender,
        "category": obj.category,
        "address_line": obj.address_line,
        "city": obj.city,
        "state": obj.state,
        "country": obj.country,
        "pincode": obj.pincode,
        "latitude": float(obj.latitude) if obj.latitude is not None else None,
        "longitude": float(obj.longitude) if obj.longitude is not None else None,
        "profile_photo_url": obj.profile_photo_url,
        "profile_photo_data": obj.profile_photo_data,  # Base64 encoded image data
        "profile_photo_mime_type": obj.profile_photo_mime_type,
    }


@router.put("/update-profile")
def update_profile(
    request: ProfileUpdateRequest,
    creds: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    data = decode_token(creds.credentials)
    uid = data.get("sub")
    if not uid:
        raise HTTPException(status_code=401, detail="invalid_token")
    
    obj = db.query(UserProfile).filter(UserProfile.id == uid).first()
    if not obj:
        raise HTTPException(status_code=404, detail="not_found")
    
    # Update profile fields
    obj.full_name = request.full_name
    obj.mobile_no = request.mobile_no
    obj.gender = request.gender
    obj.address_line = request.address_line
    obj.city = request.city
    obj.state = request.state
    obj.country = request.country
    obj.pincode = request.pincode
    
    # Update profile photo if provided
    if request.profile_photo_data:
        obj.profile_photo_data = request.profile_photo_data
        obj.profile_photo_mime_type = request.profile_photo_mime_type or 'image/jpeg'
        obj.profile_photo_url = f"data:{obj.profile_photo_mime_type};base64,{request.profile_photo_data}"
    
    db.commit()
    db.refresh(obj)
    
    return {
        "id": str(obj.id),
        "full_name": obj.full_name,
        "mobile_no": obj.mobile_no,
        "gender": obj.gender,
        "category": obj.category,
        "address_line": obj.address_line,
        "city": obj.city,
        "state": obj.state,
        "country": obj.country,
        "pincode": obj.pincode,
        "latitude": float(obj.latitude) if obj.latitude is not None else None,
        "longitude": float(obj.longitude) if obj.longitude is not None else None,
        "profile_photo_url": obj.profile_photo_url,
        "profile_photo_data": obj.profile_photo_data,
        "profile_photo_mime_type": obj.profile_photo_mime_type,
    }
