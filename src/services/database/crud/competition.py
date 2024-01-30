import uuid
from sqlmodel import Session, select, join
from services.database.models import Competition, RangeEventShooter

def create_competition(db: Session, competition: Competition):
    db_competition = Competition(**competition.model_dump())
    db.add(db_competition)
    db.commit()
    db.refresh(db_competition)
    return db_competition

def read_competitions(db: Session, offset: int = 0, limit: int = 100):
    return db.exec(select(Competition).offset(offset).limit(limit)).all()

def read_competition(db: Session, competition_id: uuid.UUID):
    return db.exec(select(Competition).filter(Competition.id == competition_id)).first()

def read_competition_shots(db: Session, competition_id: uuid.UUID):
    return db.exec(select(Competition).filter(Competition.id == competition_id)).first()
