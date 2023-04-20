def sedeEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "nombre": item ["nombre"],
        "distrito_geo": item["distrito_geo"],
        "distrito_adm": item["distrito_adm"],
        "pais": item["pais"]
    }
    
def sedesEntity(entity) -> list:
    return [sedeEntity(item) for item in entity]
