from src.model.configs.base import Base
from sqlalchemy import Colum, String, Integer

class Eventos(Base):
    __tablename__ = "Eventos"

    id= Colum(Integer, primary_key=True, autoincrement=True)
    nome = Colum(String, nullable= False) 