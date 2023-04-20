from pydantic import BaseModel
from typing import Optional

class Sede(BaseModel):
    id: Optional[str]
    nombre:str
    distrito_geo:str
    distrito_adm: str
    pais:str
