import os
import uuid
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

#Настройка БД 
DB_PATH = "/app/data/shorturl.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#Модели БД
class URLItem(Base):
    __tablename__ = "urls"
    short_id = Column(String, primary_key=True, index=True)
    full_url = Column(String, index=True)

Base.metadata.create_all(bind=engine)

#Схемы
class URLCreate(BaseModel):
    url: str

class URLStats(BaseModel):
    short_id: str
    full_url: str

#Приложение
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten")
def shorten_url(item: URLCreate, db: Session = Depends(get_db)):

    short_id = str(uuid.uuid4())[:8]
    db_obj = URLItem(short_id=short_id, full_url=item.url)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
   
    return {"short_url": f"http://localhost:8001/{short_id}", "short_id": short_id}

@app.get("/{short_id}")
def redirect_to_full(short_id: str, db: Session = Depends(get_db)):
    url_item = db.query(URLItem).filter(URLItem.short_id == short_id).first()
    if url_item is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=url_item.full_url)

@app.get("/stats/{short_id}", response_model=URLStats)
def get_stats(short_id: str, db: Session = Depends(get_db)):
    url_item = db.query(URLItem).filter(URLItem.short_id == short_id).first()
    if url_item is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return URLStats(short_id=url_item.short_id, full_url=url_item.full_url)
