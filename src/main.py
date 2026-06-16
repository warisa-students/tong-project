from fastapi import Depends, FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .database import get_db
from .model import SensorData

app = FastAPI()


class ItemCreate(BaseModel):
    name: str
    value: float


class ItemResponse(BaseModel):
    id: int
    name: str
    value: float

    class Config:
        from_attributes = True


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/dbtest")
def db_test(db: Session = Depends(get_db)):
    sensor_data = db.query(SensorData).all()
    return {"sensor_data": sensor_data}


@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = SensorData(name=item.name, value=item.value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
