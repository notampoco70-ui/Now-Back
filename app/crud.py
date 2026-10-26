from sqlalchemy.orm import Session
from . import models, schemas

def create_LostItem(db: Session, item: schemas.LostItemCreate):
    db_item = models.LostItem(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_LostItem(db: Session, item_id: int):
    return db.query(models.LostItem).filter(models.LostItem.id == item_id).first()

def get_LostItems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.LostItem).offset(skip).limit(limit).all()

def update_LostItem(db: Session, item_id: int, item: schemas.LostItemUpdate):
    db_item = db.query(models.LostItem).filter(models.LostItem.id == item_id).first()
    if db_item:
        update_data = item.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

