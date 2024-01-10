import uuid
from sqlmodel import Session, select 
from services.database.models import Event

def create_event(db: Session, event: Event):
    db_event = Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

def read_events(db: Session, offset: int = 0, limit: int = 100):
    return db.exec(select(Event).offset(offset).limit(limit)).all()

def read_event(db: Session, event_id: uuid.UUID):
    return db.exec(select(Event).filter(Event.id == event_id)).first()
