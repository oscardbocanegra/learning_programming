from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hola fastAPI!"

@app.get("/url")
async def url():
    return {"url" : "https://github.com/oscardbocanegra" }
