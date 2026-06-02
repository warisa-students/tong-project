# models.py
from sqlalchemy import Column, Integer, String, Float
from .database import Base


class SensorData(Base):
    __tablename__ = "sensor_data"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    value = Column(Float, unique=True, index=True)
