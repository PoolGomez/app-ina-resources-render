from fastapi import APIRouter, Response,status
from config.db import conn
from schemas.himno import himnoEntity, himnosEntity
from models.himno import Himno
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

himno =APIRouter()

@himno.get('/himnos')
def find_all_himno():
    return himnosEntity(conn.himno.find())

@himno.post('/himnos')
def create_himno(himno: Himno):
    new_himno = dict(himno)
    del new_himno["id"]
    
    temp_himnoParrafo = new_himno["parrafos"]
    new_himno["parrafos"] =[]
    
    for parrafo in temp_himnoParrafo:
        parrafo_dict =dict(parrafo)
        new_himno["parrafos"].append(parrafo_dict)
    
    new_id = conn.himno.insert_one(new_himno).inserted_id
    himno2 = conn.himno.find_one({"_id":new_id})
    return himnoEntity(himno2)

@himno.get('/himnos/{id}')
def find_sede(id: str):
    return himnoEntity(conn.himno.find_one({"_id":ObjectId(id)}))

@himno.put('/himnos/{id}')
def update_sede(id:str, himno: Himno):
    return "pendiente"

@himno.delete('/himnos/{id}')
def delete_himno(id: str):
    himnoEntity(conn.himno.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

    
#SEGUNDA FORMA 
# @himno.post('/himnos')
# def create_himno(himno: Himno):
#     new_himno = dict(himno)
#     del new_himno["id"]
#     temp_himnoParrafo = new_himno["parrafos"]
#     new_himno["parrafos"] =[]
#     new_id = conn.himno.insert_one(new_himno).inserted_id
#     for parrafo in temp_himnoParrafo:
#         parrafo_dict =dict(parrafo)
#         conn.himno.update_one({"_id":new_id},{"$push": { "parrafos": parrafo_dict}})
#     #id = conn.himno.insert_one(new_himno).inserted_id
#     himno2 = conn.himno.find_one({"_id":new_id})
#     return himnoEntity(himno2)