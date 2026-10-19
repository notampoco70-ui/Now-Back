from sqlalchemy import Column, Integer, String, DateTime 
from datetime import datetime 
from app.database import Base

class LostItem(Base):
    __tablename__ = "lost_items"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    location_found = Column(String, nullable=True)
    status = Column(String, default="Lost")
    item_type = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    image_url = Column(String, nullable=True, default=None)
    created_at = Column(DateTime, default=datetime.utcnow)
    