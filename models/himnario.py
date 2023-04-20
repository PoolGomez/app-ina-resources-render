from pydantic import BaseModel
from typing import Optional

class Himnario(BaseModel):
    id: Optional[str]
    codigo:int
    nombre:str
    navigate:str
    imagen_url: str

