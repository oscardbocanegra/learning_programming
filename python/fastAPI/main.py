from fastapi import FastAPI
from routers import products, users
from fastapi.staticfiles import StaticFiles  

app = FastAPI()

app.include_router(products.router)
app.include_router( users.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "Hola fastAPI!"

@app.get("/url")
async def url():
    return {"url" : "https://github.com/oscardbocanegra" }
