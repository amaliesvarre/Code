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

from pages import router as pages_router
from matching import router as matching_router

app.include_router(pages_router)
app.include_router(matching_router)