from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

user = APIRouter()

@user.get('/users')
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post('/users')
def create_user(user: User):
    hasched_password = pwd_context.hash(user.password)
    new_user = user.dict()
    new_user["password"] = hasched_password
    result = conn.execute(users.insert().values(new_user))
    print(result)
    return "hola"

@user.get('/users')
def hello():
    return "hola"

@user.get('/users')
def hello():
    return "hola"