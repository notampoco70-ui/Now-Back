from pydantic import BaseModel
from datetime import datetime
from typing import Optional

#Validate incoming and outgoing data in JSON format for lost items

class LostItemBase(BaseModel):
    title: str
    description: str
    location_found: str
    item_type: str
    phone_number: str
    image_url: Optional[str] = None

class LostItemCreate(LostItemBase):
    pass

class LostItemResponse(LostItemBase):
    id: int
    created_at: datetime
    status: str
    class Config:
        from_attributes = True

class LostItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    location_found: Optional[str] = None
    item_type: Optional[str] = None
    phone_number: Optional[str] = None
    image_url: Optional[str] = None
    status: Optional[str] = None