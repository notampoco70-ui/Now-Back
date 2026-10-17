import os
from fastapi import FastAPI
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

app = FastAPI(title="Sistema de Objetos Perdidos")

SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")

@app.get("/")
def inicio():
    return {
        "message": "Welcome to the Now back API!",
        "secret_status": f"Secret loaded key is: {SECRET_KEY}"
    }