from pydantic import BaseModel
from typing import Optional

class HimnoFav(BaseModel):
    id: Optional[str]
    id_himno:str
    id_himnario:str
    
class DataUser(BaseModel):
    id: Optional[str]
    id_user:str
    nombre:str
    email:str
    himnos: list(HimnoFav)
    
