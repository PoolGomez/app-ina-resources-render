def dataUserEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "id_user": item ["id_user"],
        "nombre": item["nombre"],
        "email": item["email"],
        "himnos": item["himnos"],
    }
    
def dataUsersEntity(entity) -> list:
    return [dataUserEntity(item) for item in entity]



# class HimnoFav(BaseModel):
#     id: Optional[str]
#     id_himno:str
#     id_himnario:str
    
# class DataUser(BaseModel):
#     id: Optional[str]
#     id_user:str
#     nombre:str
#     email:str
#     himnos: list(HimnoFav)