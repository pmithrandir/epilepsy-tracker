from fastapi import FastAPI

from api.v1 import seizures, patients
from models.orm import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(seizures.router)
app.include_router(patients.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
