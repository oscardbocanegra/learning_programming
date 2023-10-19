from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabel: bool
    
class UserDB(User):
    password : str
    
users_db = {
    "oscarbocanegra" : {
        "username": "oscarbocanegra",
        "full_name": "Oscar Bocanegra",
        "email": "davidbocanegrac@gmail.com",
        "disable": False,
        "passwor": "123456"
    },
    "oscarbocanegra2" : {
        "username": "oscarbocanegra2",
        "full_name": "Oscar Bocanegra 2",
        "email": "davidbocanegrac2@gmail.com",
        "disable": True,
        "passwor": "654321"
    }
}

def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])