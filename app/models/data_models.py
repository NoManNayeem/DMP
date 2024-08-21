from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from ..database import Base

class FirstPartyData(Base):
    __tablename__ = "first_party_data"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    data = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    class Config:
        from_attributes = True

class SecondPartyData(Base):
    __tablename__ = "second_party_data"

    id = Column(Integer, primary_key=True, index=True)
    partner_id = Column(String, index=True)
    data = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    class Config:
        from_attributes = True

class ThirdPartyData(Base):
    __tablename__ = "third_party_data"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    data = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    class Config:
        from_attributes = True
