import datetime

from pydantic import BaseModel


class SeizureBase(BaseModel):
    timestamp_start: datetime.datetime
    timestamp_end: datetime.datetime
    patient_id: int


class SeizureCreate(SeizureBase):
    pass


class Seizure(SeizureBase):
    id: int

    class Config:
        orm_mode = True
