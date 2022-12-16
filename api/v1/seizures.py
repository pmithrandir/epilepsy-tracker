from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.v1.crud import *
from models.business import seizure as seizure_business
from models.business.patient import Patient
from models.orm import get_db
from models.orm.seizure import Seizure

router = APIRouter(
    prefix="/seizures",
    tags=["seizures"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_seizures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    seizures = get_all_from_orm(Seizure, db, skip=skip, limit=limit)
    return seizures


@router.get("/{seizure_id}", response_model=seizure_business.Seizure)
async def read_seizure(seizure_id: int, db: Session = Depends(get_db)):
    db_object = get_from_orm(Seizure, db, object_id=seizure_id)
    if db_object is None:
        raise HTTPException(status_code=404, detail="Seizure not found")
    return db_object


@router.post("/", response_model=seizure_business.Seizure)
def create_seizure(seizure: seizure_business.SeizureCreate, db: Session = Depends(get_db)):
    return create_in_orm(Seizure, db=db, seizure=seizure)
