from pydantic import BaseModel,Field
from typing import Optional,List

class Parrafo(BaseModel):
    id:int
    nro_parrafo: str
    contenido: str

class Himno(BaseModel):
    id: Optional[str]
    id_himnario: int
    numero : int
    titulo : str
    tipo: str
    numero_parrafos: int
    autor:str
    comentario: str
    video:str
    parrafos: List[Parrafo] #=Field(default_factory=list)
    #parrafos: list[Parrafo]
