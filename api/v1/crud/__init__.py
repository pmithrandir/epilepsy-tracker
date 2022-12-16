from pydantic import BaseModel
from sqlalchemy.orm import Session

from models.orm import Base


def get_from_orm(my_class: Base, db: Session, object_id: int):
    return db.query(my_class).get(object_id)


def get_all_from_orm(my_class: Base, db: Session, skip: int = 0, limit: int = 100):
    return db.query(my_class).offset(skip).limit(limit).all()


def __find_foreign_keys(foreign_keys):
    foreign_keys_detected = {}
    for param, value in foreign_keys.items():
        if type(value) is int:
            foreign_keys_detected[param] = value
        else:
            if len(value.__table__.primary_key) > 1:
                raise ValueError("too many pk detected")
            elif len(value.__table__.primary_key) == 0:
                raise ValueError("no pk detected")
            else:
                foreign_keys_detected[param] = getattr(value, list(value.__table__.primary_key)[0].name)


def create_in_orm(my_class: Base, db: Session, pydantic_object: BaseModel, **foreign_keys):
    if not pydantic_object.__class__.__name__.endswith("Create"):
        raise ValueError(f"invalid pydantic class")
    if pydantic_object.__class__.__name__ != my_class.__nama__ + "Create":
        raise ValueError(f"Pydantic class not related to ORM class")

    if foreign_keys is None:
        db_object = my_class(**pydantic_object.dict())
    else:
        foreign_keys_detected = __find_foreign_keys(foreign_keys)
        db_object = my_class(
            **pydantic_object.dict(),
            **foreign_keys_detected
        )
    db.add(db_object)
    db.commit()
    db.refresh(db_object)
    return db_object
