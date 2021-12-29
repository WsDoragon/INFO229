from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .database import Base #Se importa el objeto Base desde el archivo database.py

class News(Base): 

    __tablename__ = "news"

    id_news = Column(Integer, primary_key=True, index=True)
    title = Column(String(500))
    url = Column(String(500))
    date = Column(String(500))
    media_outlet = Column(String(500))
    category =  Column(String(500))