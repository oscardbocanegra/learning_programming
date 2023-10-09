from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    lastname: str
    url: str
    age: int
    
users_list = [User(name = "Oscar", lastname = "Bocanegra", url = "https://github.com/oscardbocanegra", age = 19 ), 
              User(name = "David", lastname = "Capera", url = "https://github.com/davidcapera", age = 22),
              User(name = "Juan", lastname = "Lopez", url = "https://github.com/juanlopez", age = 45)]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Oscar", "lastname": "Bocanegra", "url" : "https://github.com/oscardbocanegra", "age":19},
            {"name": "David", "lastname": "Capera", "url" : "https://github.com/davidcapera", "age":22},
            {"name": "Juan", "lastname": "Lopez", "url" : "https://github.com/juanlopez", "age":45}]
    
    
@app.get("/users")
async def users():
    return users_list