from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from database import SessionLocal
import models

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
def despesas_operadora(cnpj: str, db: Session = Depends(get_db)):
    return db.query(models.DespesaConsolidada)\
        .filter_by(cnpj=cnpj)\
        .all()

@app.get("/api/estatisticas")
def estatisticas(db: Session = Depends(get_db)):
    return db.execute("""
        SELECT uf, SUM(total_despesas)
        FROM despesas_agregadas
        GROUP BY uf
    """).fetchall()
