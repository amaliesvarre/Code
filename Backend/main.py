from fastapi import FastAPI

from database import Base, engine
from auth import router as auth_router
from matching import router as matching_router
from pages import router as pages_router
from simulations import router as simulations_router
import models

app = FastAPI(title="CENet Backend")

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(matching_router)
app.include_router(pages_router)
app.include_router(simulations_router)


@app.get("/")
def root():
    return {"message": "CENet backend is running"}