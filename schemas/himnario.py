def himnarioEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "codigo":item["codigo"],
        "nombre": item ["nombre"],
        "navigate": item["navigate"],
        "imagen_url": item["imagen_url"],
    }
    
def himnariosEntity(entity) -> list:
    return [himnarioEntity(item) for item in entity]