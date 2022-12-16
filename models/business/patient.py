import datetime
from typing import List

from pydantic import BaseModel

from models.business.seizure import Seizure


class PatientBase(BaseModel):
    firstname: str
    lastname: str


class PatientCreate(PatientBase):
    pass


class Patient(PatientBase):
    id: int
    seizures: List[Seizure] = []

    class Config:
        orm_mode = True
