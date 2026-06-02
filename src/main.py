from fastapi import FastAPI
from .database import get_db

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/dbtest")
def db_test():
    db = get_db()

    return {"message": "Database connection successful"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
