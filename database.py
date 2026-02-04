from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:senha@localhost/teste_intuitive"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
