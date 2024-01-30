import uuid
from sqlmodel import Session, select 
from services.database.models import Discipline

def create_discipline(db: Session, discipline: Discipline):
    db_discipline = Discipline(**discipline.model_dump())
    db.add(db_discipline)
    db.commit()
    db.refresh(db_discipline)
    return db_discipline

def read_disciplines(db: Session, offset: int = 0, limit: int = 100):
    return db.exec(select(Discipline).offset(offset).limit(limit)).all()

def read_discipline(db: Session, discipline_id: uuid.UUID):
    return db.exec(select(Discipline).filter(Discipline.id == discipline_id)).first()
