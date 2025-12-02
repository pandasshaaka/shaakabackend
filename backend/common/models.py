from sqlalchemy import Column, String, Text, TIMESTAMP, Numeric, text
from sqlalchemy.dialects.postgresql import UUID
from .db import Base


class UserProfile(Base):
    __tablename__ = "user_profiles"
    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text("gen_random_uuid()"))
    full_name = Column(String(255), nullable=False)
    mobile_no = Column(String(20), nullable=False, unique=True)
    password = Column(Text, nullable=False)
    gender = Column(String(20))
    category = Column(String(50), nullable=False)
    address_line = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    country = Column(String(100))
    pincode = Column(String(20))
    latitude = Column(Numeric(10, 7))
    longitude = Column(Numeric(10, 7))
    profile_photo_url = Column(Text)
    created_at = Column(TIMESTAMP, server_default=text("NOW()"))
    updated_at = Column(TIMESTAMP, server_default=text("NOW()"))
