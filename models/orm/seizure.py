from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from . import Base


class Seizure(Base):
    __tablename__ = "seizures"

    id = Column(Integer, primary_key=True, index=True)
    timestamp_start = Column(DateTime, index=True)
    timestamp_end = Column(DateTime, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))

    patient = relationship("Patient", back_populates="seizures")
