from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth import get_db, get_current_user, require_role
import models
import schemas

router = APIRouter(prefix="/matching", tags=["Matching"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_match_request(
    request: schemas.MatchRequestCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role(["user"]))
):
    db_request = models.MatchRequest(
        user_id=current_user.id,
        province=request.province,
        need_type=request.need_type,
        message=request.message,
        status="pending"
    )

    db.add(db_request)
    db.commit()
    db.refresh(db_request)

    return {
        "message": "Match request created successfully",
        "match_request": {
            "id": db_request.id,
            "user_id": db_request.user_id,
            "province": db_request.province,
            "need_type": db_request.need_type,
            "message": db_request.message,
            "status": db_request.status
        }
    }


@router.get("/my-requests")
def get_my_match_requests(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role(["user"]))
):
    requests = (
        db.query(models.MatchRequest)
        .filter(models.MatchRequest.user_id == current_user.id)
        .all()
    )

    return requests


@router.get("/all")
def get_all_match_requests(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(require_role(["operator", "supplier"]))
):
    requests = db.query(models.MatchRequest).all()
    return requests