from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy import create_engine, Column, Float, Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
import uvicorn
from pydantic import BaseModel
from datetime import datetime

# Database Configuration
DATABASE_URL = "mysql+pymysql://root:mypassword#@localhost/weather_station"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Model Definition
class Reading(Base):
    __tablename__ = "readings"

    id = Column(Integer, primary_key=True, index=True)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    pressure = Column(Float, nullable=False)
    altitude = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, server_default='CURRENT_TIMESTAMP', nullable=False)

# Create the database tables
Base.metadata.create_all(bind=engine)

# FastAPI application
app = FastAPI()

# Mount static files and set up templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Pydantic model for request validation
class ReadingCreate(BaseModel):
    temperature: float
    humidity: float
    pressure: float
    altitude: float
    timestamp: datetime

class ReadingResponse(BaseModel):
    id: int
    temperature: float
    humidity: float
    pressure: float
    altitude: float
    timestamp: datetime

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoint to create a reading
@app.post("/readings/", response_model=ReadingResponse)
async def create_reading(reading: ReadingCreate, db: Session = Depends(get_db)):
    db_reading = Reading(**reading.dict())
    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)
    return db_reading

# API Endpoint to get the most recent readings
@app.get("/readings/")
async def get_readings(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Reading).order_by(Reading.timestamp.desc()).offset(skip).limit(limit).all()

# Root endpoint to serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
