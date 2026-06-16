import asyncio
from contextlib import asynccontextmanager
from .database import SessionLocal
from fastapi import FastAPI
from .model import SensorData
import random


async def continuous_monitor():
    """A background process that runs forever while the app is alive."""
    try:
        while True:
            print("Sensor Data Incoming...")
            db = SessionLocal()
            try:
                random_value = random.uniform(20.0, 30.0)
                data = SensorData(name="Temperature", value=random_value)
                db.add(data)
                db.commit()
            finally:
                db.close()
            await asyncio.sleep(3)
    except asyncio.CancelledError:
        print("Background task was cleanly cancelled.")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Start the continuous process on app startup
    task = asyncio.create_task(continuous_monitor())
    yield
    # 2. Gracefully cancel the process when the app shuts down
    task.cancel()
    await asyncio.gather(task, return_exceptions=True)
