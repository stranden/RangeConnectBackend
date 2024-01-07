import uuid
from sqlmodel import Session, select 
from services.database.models import ShootingClub

def create_club(db: Session, shooting_club: ShootingClub):
    db_shooting_club = ShootingClub(**shooting_club.model_dump())
    db.add(db_shooting_club)
    db.commit()
    db.refresh(db_shooting_club)
    return db_shooting_club

def read_club(db: Session, shooting_club_id: uuid.UUID):
    return db.exec(select(ShootingClub).filter(ShootingClub.id == shooting_club_id).first())

def read_clubs(db: Session, skip: int = 0, limit: int = 10):
    return db.exec(select(ShootingClub).offset(skip).limit(limit)).all()

#def update_item(db: Session, item_id: int, updated_item: Item):
#    db_item = db.query(Item).filter(Item.id == item_id).first()
#    if db_item:
#        for key, value in updated_item.dict().items():
#            setattr(db_item, key, value)
#        db.commit()
#        db.refresh(db_item)
#    return db_item
#
#def delete_item(db: Session, item_id: int):
#    db_item = db.query(Item).filter(Item.id == item_id).first()
#    if db_item:
#        db.delete(db_item)
#        db.commit()
#    return db_item
