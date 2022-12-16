from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from . import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)

    seizures = relationship("Seizure", back_populates="patient")

