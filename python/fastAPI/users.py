from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/users")
async def usersjson():
    return [{"name": "Oscar", "lastname": "Bocanegra", "url" : "https://github.com/oscardbocanegra"},
            {"name": "David", "lastname": "Capera", "url" : "https://github.com/davidcapera"},]