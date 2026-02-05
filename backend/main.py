from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal
import models
from models import Operadora, DespesasConsolidadas
from sqlalchemy import func
from fastapi import Depends


app = FastAPI(title="API Operadoras")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Listagem das rotas de API

@app.get("/api/operadoras")
def listar_operadoras(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit

    return db.query(models.Operadora)\
        .offset(offset)\
        .limit(limit)\
        .all()

@app.get("/api/operadoras/{cnpj}")
def detalhe_operadora(cnpj: str, db: Session = Depends(get_db)):
    return db.query(models.Operadora)\
        .filter_by(cnpj=cnpj)\
        .first()

@app.get("/api/operadoras/{cnpj}/despesas")
def get_despesas_operadora(cnpj: str, db: Session = Depends(get_db)):
    despesas = (
        db.query(DespesasConsolidadas)
        .filter(DespesasConsolidadas.cnpj == cnpj)
        .all()
    )

    return despesas or []


@app.get("/api/estatisticas")
def get_estatisticas(db: Session = Depends(get_db)):
    total = db.query(func.sum(DespesasConsolidadas.valor_despesas)).scalar()
    media = db.query(func.avg(DespesasConsolidadas.valor_despesas)).scalar()

    top_5 = (
        db.query(
            Operadora.razao_social,
            func.sum(DespesasConsolidadas.valor_despesas).label("total")
        )
        .join(
            DespesasConsolidadas,
            Operadora.cnpj == DespesasConsolidadas.cnpj
        )
        .group_by(Operadora.razao_social)
        .order_by(func.sum(DespesasConsolidadas.valor_despesas).desc())
        .limit(5)
        .all()
    )

    return {
        "total_despesas": float(total or 0),
        "media_despesas": float(media or 0),
        "top_5_operadoras": [
            {"razao_social": r, "total": float(t)}
            for r, t in top_5
        ]
    }

