from fastapi import FastAPI
from routers import products, users

app = FastAPI()

app.include_router(products.router)
app.include_router( users.router)

@app.get("/")
async def root():
    return "Hola fastAPI!"

@app.get("/url")
async def url():
    return {"url" : "https://github.com/oscardbocanegra" }
