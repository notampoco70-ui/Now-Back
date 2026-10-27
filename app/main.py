import os
from fastapi import FastAPI, Depends, HTTPException
from dotenv import load_dotenv
from .database import engine, Base, get_db
from . import models, schemas, crud
from sqlalchemy.orm import Session




# Load environment variables from .env file and create database tables
load_dotenv()
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Lost item Now Back API")

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

# Define a simple route to test the API
@app.get("/")
def inicio():
    return {
        "message": "Welcome to the Now Back API!",
        "secret_status": f"Secret loaded key is: {SECRET_KEY}"
    }

# Define a route to create a report for a lost item
@app.post("/lost_items/", response_model=schemas.LostItemResponse)
def create_item(item: schemas.LostItemCreate, db: Session = Depends(get_db)):
    return crud.create_LostItem(db=db, item=item)

@app.get("/lost_items/" , response_model=list[schemas.LostItemResponse])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_LostItems(db, skip=skip, limit=limit)
    return items

@app.get("/lost_items/{item_id}", response_model=schemas.LostItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get_LostItem(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/lost_items/{item_id}", response_model=schemas.LostItemResponse)
def update_item(item_id: int, item: schemas.LostItemUpdate, db: Session = Depends(get_db)):
    db_item = crud.update_LostItem(db, item_id=item_id, item=item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/lost_items/{item_id}", response_model=schemas.LostItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete_LostItem(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_User(db=db, user=user)

@app.get("/users/", response_model=list[schemas.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_Users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_User(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/users/{user_id}", response_model=schemas.UserResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_User(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.UserResponse)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_User(db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


