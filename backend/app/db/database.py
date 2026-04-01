from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:Befeelg15!@localhost:5432/schemesense"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)