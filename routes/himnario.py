from fastapi import APIRouter, Response,status
from config.db import conn
from schemas.himnario import himnarioEntity, himnariosEntity
from models.himnario import Himnario
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

himnario =APIRouter()

@himnario.get('/himnarios')
def find_all_himnario():
    return himnariosEntity(conn.himnario.find())

@himnario.post('/himnarios')
def create_himnario(himnario: Himnario):
    new_himnario = dict(himnario)
    del new_himnario["id"]
    id = conn.himnario.insert_one(new_himnario).inserted_id
    himnario = conn.himnario.find_one({"_id":id})
    return himnarioEntity(himnario)
    
@himnario.get('/himnarios/{id}')
def find_himnario(id: str):
    return himnarioEntity(conn.himnario.find_one({"_id":ObjectId(id)}))

@himnario.put('/himnarios/{id}')
def update_himnario(id:str, himnario: Himnario):
    conn.himnario.find_one_and_update({"_id":ObjectId(id)}, {"$set": dict(himnario)})
    return himnarioEntity(conn.himnario.find_one({"_id":ObjectId(id)}))

@himnario.delete('/himnarios/{id}')
def delete_himnario(id: str):
    himnarioEntity(conn.himnario.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)