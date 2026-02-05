from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:280904@localhost:5432/teste_intuitive"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
