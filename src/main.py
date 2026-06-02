from fastapi import Depends, FastAPI
from .database import get_db
from .model import SensorData

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/dbtest")
# def db_test(db=Depends(get_db)):
def db_test():
    db = next(get_db())
    sensor_data = db.query(SensorData).all()
    return {"sensor_data": sensor_data}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
