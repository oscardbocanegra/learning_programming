from fastapi import APIRouter, Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt 
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "8a7124c49db9744d1d7a2dbed23a6a05025ea3720891a1a6099e60fe7fffef35"

app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

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
        "password" : "$2a$12$3Vuv1xPy1A0dE8UWDXwmxuiQx/oxFqlOto6eur8ltpgrzWDXNfhfS"
    },
    "davidbocanegra": {
        "username": "davidbocanegra",
        "full_name": "Oscar David Bocanegra Capera",
        "email": "davidbocanegrac@gmail.com",
        "disable": False,
        "password" : "$2a$12$MFXt85S2iI5mjpaeNLn7/eVqGnSVXqqLa.GvrdM/Vkyr.P1vxSV9a"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")

    user = search_user_db(form.username)
    
    
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET ,algorithm=ALGORITHM), "token_type": "bearer"}