from pydantic import BaseModel


class ItemCreate(BaseModel):
    name: str
    value: float


class ItemResponse(BaseModel):
    id: int
    name: str
    value: float

    class Config:
        from_attributes = True
