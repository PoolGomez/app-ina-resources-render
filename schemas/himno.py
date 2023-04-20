def parrafoEntity(parrafo) -> dict:
    return {
        "id":str(parrafo["id"]),
        "nro_parrafo":parrafo["nro_parrafo"],
        "contenido":parrafo["contenido"],
    }
def parrafosEntity(p)->list:
    return [parrafoEntity(i) for i in p]

def himnoEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "id_himnario": str(item ["id_himnario"]),
        "numero": str(item["numero"]),
        "titulo": item["titulo"],
        "tipo": item["tipo"],
        "numero_parrafos": str(item ["numero_parrafos"]),
        "autor": item["autor"],
        "comentario": item["comentario"],
        "video": item["video"],
        "parrafos": parrafosEntity(item["parrafos"])
        #"parrafos": item["parrafos"]
    }
    
def himnosEntity(entity) -> list:
    return [himnoEntity(item) for item in entity]


# class Parrafo(BaseModel):
#     id:Optional[int]
#     nro_parrafo: str
#     contenido: str

# class Himno(BaseModel):
#     id: Optional[str]
#     id_himnario: str
#     numero : int
#     titulo : str
#     tipo: str
#     numero_parrafos: int
#     autor:str
#     comentario: str
#     video:str
#     parrafos: list(Parrafo)