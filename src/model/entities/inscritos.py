from src.model.configs.base import Base
from sqlalchemy import Colum, String, Integer, ForeignKey

class Inscritos(Base):
    __tablename__ = "Inscritos"

    id= Colum(Integer, primary_key=True, autoincrement=True)
    nome = Colum(String, nullable= False) 
    email = Colum(String, nullable= False)
    link = Colum(String, nullable= True)
    evento_id = Colum (Integer, ForeignKey("Eventos.id"))

