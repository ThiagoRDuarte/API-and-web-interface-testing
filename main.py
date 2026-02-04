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
