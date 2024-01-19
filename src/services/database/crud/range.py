import uuid
from sqlmodel import Session, select 
from services.database.models import ShootingRange

def create_shooting_range(db: Session, shooting_range: ShootingRange):
    db_shooting_range = ShootingRange(**shooting_range.model_dump())
    db.add(db_shooting_range)
    db.commit()
    db.refresh(db_shooting_range)
    return db_shooting_range

def read_shooting_ranges(db: Session, offset: int = 0, limit: int = 100):
    return db.exec(select(ShootingRange).offset(offset).limit(limit)).all()

def read_shooting_range(db: Session, shooting_range_id: uuid.UUID):
    return db.exec(select(ShootingRange).filter(ShootingRange.id == shooting_range_id)).first()
