from sqlalchemy.orm import Session

from models.business import seizure as seizure_business
from models.orm import seizure as seizure_orm


def get_seizure(db: Session, seizure_id: int):
    return db.query(seizure_orm.Seizure).filter(seizure_orm.Seizure.id == seizure_id).first()


def get_seizures(db: Session, skip: int = 0, limit: int = 100):
    return db.query(seizure_orm.Seizure).offset(skip).limit(limit).all()


def create_seizure(db: Session, seizure: seizure_business.SeizureCreate):
    db_seizure = seizure_orm.Seizure(
        timestamp_start=seizure.timestamp_start,
        timestamp_end=seizure.timestamp_end,
        patient_id=seizure.patient_id
    )
    db.add(db_seizure)
    db.commit()
    db.refresh(db_seizure)
    return db_seizure
