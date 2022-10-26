
from sqlalchemy.orm import Session
from . import models, schemas

def get_users(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

