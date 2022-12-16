from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.v1.crud import *
from models.business import patient as patient_business
from models.orm import get_db
from models.orm.patient import Patient

router = APIRouter(
    prefix="/patients",
    tags=["patients"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
def read_patients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    patients = get_all_from_orm(Patient, db, skip=skip, limit=limit)
    return patients


@router.get("/{patient_id}", response_model=patient_business.Patient)
async def read_patient(patient_id: int, db: Session = Depends(get_db)):
    db_object = get_from_orm(Patient, db, object_id=patient_id)
    if db_object is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return db_object


@router.post("/", response_model=patient_business.Patient)
def create_patient(patient: patient_business.PatientCreate, db: Session = Depends(get_db)):
    return create_in_orm(Patient, db=db, patient=patient)
