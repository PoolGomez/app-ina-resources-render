from fastapi import APIRouter, Response,status
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

user =APIRouter()

#@user.get('/users',response_model=list[User], tags=["users"])
@user.get('/users')
def find_all_user():
    return usersEntity(conn.user.find())

#@user.post('/users',response_model=User, tags=["users"])
@user.post('/users')
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.user.insert_one(new_user).inserted_id
    user = conn.user.find_one({"_id":id})
    return userEntity(user)
    
#@user.get('/users/{id}',response_model=User, tags=["users"])
@user.get('/users/{id}')
def find_user(id: str):
    return userEntity(conn.user.find_one({"_id":ObjectId(id)}))

#@user.put('/users/{id}',response_model=User, tags=["users"])
@user.put('/users/{id}')
def update_user(id:str, user: User):
    conn.user.find_one_and_update({"_id":ObjectId(id)}, {"$set": dict(user)})
    return userEntity(conn.user.find_one({"_id":ObjectId(id)}))

#@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
@user.delete('/users/{id}')
def delete_user(id: str):
    userEntity(conn.user.find_one_and_delete({"_id":ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)