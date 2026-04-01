from fastapi import FastAPI
from app.db.database import engine
from app.db.base import Base
from app.models import user
from app.api.routes import auth
from app.api.routes import documents

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth")
app.include_router(documents.router, prefix="/documents")

@app.get("/")
def read_root():
    return {"message": "Welcome to SchemeSense API 🚀"}