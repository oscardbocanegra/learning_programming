from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int
    
users_list = [User(id = 1 ,name = "Oscar", lastname = "Bocanegra", url = "https://github.com/oscardbocanegra", age = 19 ), 
              User(id = 2, name = "David", lastname = "Capera", url = "https://github.com/davidcapera", age = 22),
              User(id = 3, name = "Juan", lastname = "Lopez", url = "https://github.com/juanlopez", age = 45)]

@app.get("/usersj son")
async def usersjson():
    return [{"name": "Oscar", "lastname": "Bocanegra", "url" : "https://github.com/oscardbocanegra", "age":19},
            {"name": "David", "lastname": "Capera", "url" : "https://github.com/davidcapera", "age":22},
            {"name": "Juan", "lastname": "Lopez", "url" : "https://github.com/juanlopez", "age":45}]
    
    
@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    
@app.get("/user/")
async def user(id: int):
    return search_user(id)


@app.post("/user/", status_code=201)    
async def user(user: User): 
    if type(search_user(user.id)) == User:
        return HTTPException(status_code=204, detail="El usuario ya existe")   
    
    users_list.append(user)
    return user

@app.put("/user/")
async def user(user: User):
    
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            
    if not found:
        return {"error": "No se ha actualizado el usuario"}
    else:
        return user
    
    
@app.delete("/user/{id}")
async def user(id: int):
     
    found = False
    
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            
    if not found:
        return {"error":"No se ha eliminado el usuario"}
    

    

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list) 
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}