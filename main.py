from fastapi import FastAPI
from database import engine, Base
import models
import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

