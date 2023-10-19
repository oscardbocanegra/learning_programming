from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(tags=["user"])

class User(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int
    
users_list = [User(id = 1 ,name = "Oscar", lastname = "Bocanegra", url = "https://github.com/oscardbocanegra", age = 19 ), 
              User(id = 2, name = "David", lastname = "Capera", url = "https://github.com/davidcapera", age = 22),
              User(id = 3, name = "Juan", lastname = "Lopez", url = "https://github.com/juanlopez", age = 45)]

@router.get("/usersj son")
async def usersjson():
    return [{"name": "Oscar", "lastname": "Bocanegra", "url" : "https://github.com/oscardbocanegra", "age":19},
            {"name": "David", "lastname": "Capera", "url" : "https://github.com/davidcapera", "age":22},
            {"name": "Juan", "lastname": "Lopez", "url" : "https://github.com/juanlopez", "age":45}]
    
    
@router.get("/users")
async def users():
    return users_list

@router.get("/prueba")
async def prueba():
    return "Todo ok"

@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)
    
@router.get("/user/")
async def user(id: int):
    return search_user(id)


@router.post("/user/", response_model=User ,status_code=201)    
async def user(user: User): 
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")   
    
    users_list.append(user)
    return user

@router.put("/user/")
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
    
    
@router.delete("/user/{id}")
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