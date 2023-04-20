from fastapi import APIRouter
import smtplib
from email.message import EmailMessage
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from config.db import conn

authentication =APIRouter()

@authentication.post('/recovery')
def recovery():
    email_origen = "appina.recovery@gmail.com"
    email_password = "rzpqknqayqpdwazs" #"inacantogrande9"
    email_destino = "pgomez4790@gmail.com"
    msg = EmailMessage()
    msg['Subject'] = "Email Subject"
    msg['From'] = email_origen
    msg['To'] = email_destino
    msg.set_content(
        f"""\
            Email : {email_destino}
            Message : este correo es de prueba para la app APPINA
        """,
    )
    
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(email_origen,email_password)
        smtp.send_message(msg)
    return "email enviado correctamente"

@authentication.post('/register')
def register(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.user.insert_one(new_user).inserted_id
    user = conn.user.find_one({"_id":id})
    return userEntity(user)

@authentication.get('/login')
def login(email: str, password: str):
    user_login = conn.user.find_one({"email":email,"password":password})
    return userEntity(user_login)