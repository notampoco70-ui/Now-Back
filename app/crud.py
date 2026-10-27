from sqlalchemy.orm import Session
from . import models, schemas
from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)

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

def delete_LostItem(db: Session, item_id: int):
    db_item = db.query(models.LostItem).filter(models.LostItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

def create_User(db: Session, user: schemas.UserCreate):
    user_data = user.model_dump()
    plain_password = user_data.pop("password")
    hashed_pwd = hash_password(plain_password)
    db_user = models.User(**user_data, hashed_password=hashed_pwd)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_User(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_User(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_Users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def update_User(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        user_data = user.model_dump(exclude_unset=True)
        if "password" in user_data:
            plain_pwd = user_data.pop("password")
            user_data["hashed_password"] = hash_password(plain_pwd)
            
        for key, value in user_data.items():
            setattr(db_user, key, value)
            
        db.commit()
        db.refresh(db_user)
    return db_user