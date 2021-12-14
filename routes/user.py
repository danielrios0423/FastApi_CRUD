from fastapi import APIRouter, Response
from config.db import conn
from models.user import users
from schemas.user import User
from starlette.status import HTTP_204_NO_CONTENT

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user = APIRouter()

@user.get('/users', tags= ["Users"])
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post('/users', tags= ["Users"])
def create_user(user: User):
    hasched_password = pwd_context.hash(user.password)
    new_user = user.dict()
    new_user["password"] = hasched_password
    result = conn.execute(users.insert().values(new_user))
    print(result.lastrowid)
    return conn.execute(users.select().where(users.c.id ==result.lastrowid)).first()

@user.get('/users/{id}', tags= ["Users"])
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()
    
@user.delete('/users/{id}', tags= ["Users"])
def delete_user(id: str):
    result = conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put('/users/{id}', tags= ["Users"])
def update_user(id: str, user: User):
    conn.execute(users.update().values(name = user.name, 
        email= user.email,
        password= pwd_context.hash(user.password)).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).first()

