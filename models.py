from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Operadora(Base):
    __tablename__ = "operadoras"

    cnpj = Column(String, primary_key=True)
    razao_social = Column(String)
    uf = Column(String)
