from sqlalchemy import Column, Integer, String
from database import Base

class Pokemon(Base):
    __tablename__ = "pokemons"


    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, index=True)
    image: str = Column(String)
    type: str = Column(String)