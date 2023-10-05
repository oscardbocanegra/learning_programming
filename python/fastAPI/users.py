from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def users():
    return "Place of users"