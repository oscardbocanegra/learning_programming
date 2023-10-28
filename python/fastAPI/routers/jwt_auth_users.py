from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disable: bool
    
class UserDB(User):
    password: str
    

users_db = {
    "oscarbocanegra": {
        "username": "oscarbocanegra",
        "full_name": "Oscar David Bocanegra",
        "email": "oscarbocanegra@gmail.com",
        "disable": False,
        "password" : "123456"
    },
    "davidbocanegra": {
        "username": "davidbocanegra",
        "full_name": "Oscar David Bocanegra Capera",
        "email": "davidbocanegrac@gmail.com",
        "disable": False,
        "password" : "654321"
    }
}