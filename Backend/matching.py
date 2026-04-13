from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas
from auth import get_current_user

router = APIRouter(prefix="/matching", tags=["Matching"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# CREATE MATCH REQUEST
@router.post("/", response_model=schemas.MatchRequestResponse)
def create_match(
    request: schemas.MatchRequestCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_request = models.MatchRequest(
        energy_type=request.energy_type,
        capacity=request.capacity,
        location=request.location,
        preferences=request.preferences,
        user_id=current_user.id
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)

    return new_request


# GET USER MATCHES
@router.get("/", response_model=list[schemas.MatchRequestResponse])
def get_my_matches(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.MatchRequest).filter(
        models.MatchRequest.user_id == current_user.id
    ).all()