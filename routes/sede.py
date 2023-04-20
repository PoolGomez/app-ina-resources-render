from fastapi import APIRouter, Response,status
from config.db import conn
from schemas.sede import sedeEntity, sedesEntity
from models.sede import Sede
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

sede =APIRouter()

@sede.get('/sedes')
def find_all_sede():
    return sedesEntity(conn.sede.find())

@sede.post('/sedes')
def create_sede(sede: Sede):
    new_sede = dict(sede)
    del new_sede["id"]
    id = conn.sede.insert_one(new_sede).inserted_id
    sede = conn.sede.find_one({"_id":id})
    return sedeEntity(sede)
    
@sede.get('/sedes/{id}')
def find_sede(id: str):
    return sedeEntity(conn.sede.find_one({"_id":ObjectId(id)}))

@sede.put('/sedes/{id}')
def update_sede(id:str, sede: Sede):
    conn.sede.find_one_and_update({"_id":ObjectId(id)}, {"$set": dict(sede)})
    return sedeEntity(conn.sede.find_one({"_id":ObjectId(id)}))

@sede.delete('/sedes/{id}')
def delete_sede(id: str):
    sedeEntity(conn.sede.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)