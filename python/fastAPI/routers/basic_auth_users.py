from fastapi import FastAPI, Depends, HTTPException, status
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
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales de autenticacion invalidas", 
                            headers={"WWW-Authenticate": "Bearer"})
    return user 
    
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="El usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="La contraseña no es correcto")
    
    return {"access-token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user

@app.get("/user")
async def prueba():
    return "PRUEBA"

@app.get("/test")
async def test():
    return "test done"