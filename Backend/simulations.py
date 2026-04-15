from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from auth import get_db, get_current_user
import models
import schemas

router = APIRouter(prefix="/simulations", tags=["Simulations"])


@router.post("/", response_model=schemas.SimulationResponse, status_code=status.HTTP_201_CREATED)
def create_simulation(
    simulation: schemas.SimulationCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_simulation = models.Simulation(
        user_id=current_user.id,
        title=simulation.title,
        input_data=simulation.input_data,
        result_data=None
    )

    db.add(db_simulation)
    db.commit()
    db.refresh(db_simulation)

    return db_simulation


@router.get("/", response_model=list[schemas.SimulationResponse])
def get_my_simulations(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    simulations = (
        db.query(models.Simulation)
        .filter(models.Simulation.user_id == current_user.id)
        .order_by(models.Simulation.created_at.desc())
        .all()
    )
    return simulations


@router.get("/{simulation_id}", response_model=schemas.SimulationResponse)
def get_simulation_by_id(
    simulation_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    simulation = (
        db.query(models.Simulation)
        .filter(
            models.Simulation.id == simulation_id,
            models.Simulation.user_id == current_user.id
        )
        .first()
    )

    if simulation is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Simulation not found"
        )

    return simulation