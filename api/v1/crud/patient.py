from sqlalchemy.orm import Session

from models.business import patient as patient_business
from models.orm import patient as patient_orm


def get_patient(db: Session, patient_id: int):
    return db.query(patient_orm.Patient).filter(patient_orm.Patient.id == patient_id).first()


def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(patient_orm.Patient).offset(skip).limit(limit).all()


def create_patient(db: Session, patient: patient_business.PatientCreate):
    db_patient = patient_orm.Patient(firstname=patient.firstname, lastname=patient.lastname)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
