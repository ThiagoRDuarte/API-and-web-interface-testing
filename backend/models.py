from sqlalchemy import Column, String, Integer, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Operadora(Base):
    __tablename__ = "operadoras"

    cnpj = Column(String, primary_key=True)
    razao_social = Column(String, nullable=False)
    uf = Column(String)

    despesas = relationship("DespesasConsolidadas", back_populates="operadora")


class DespesasConsolidadas(Base):
    __tablename__ = "despesas_consolidadas"

    id = Column(Integer, primary_key=True, index=True)
    cnpj = Column(String, ForeignKey("operadoras.cnpj"))
    valor_despesas = Column(Numeric)

    operadora = relationship("Operadora", back_populates="despesas")
