from pydantic import BaseModel

class PropertyDetails(BaseModel):
    owner_id: int
    name: str
    type: str
    nunits: int
    floors: int

class PName(BaseModel):
    name: str