from sqlalchemy.orm import Session
from sqlalchemy import and_
from . import models


def get_all_news(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.News).offset(skip).limit(limit).all()

def get_news(db: Session, from_: str = '2021-10-01', to_: str = '2021-10-20', category: str = '', limit: int = 100):
    return db.query(models.News).filter(and_(models.News.date >= from_, models.News.date <= to_, models.News.category == category)).limit(limit).all()
