import os
from fastapi import FastAPI
from dotenv import load_dotenv
from .database import engine, Base
from . import models


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
    
