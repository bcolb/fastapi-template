from fastapi import FastAPI

from app.db import database, User

app = FastAPI(title="FastAPI Template")

@app.get("/")
async def read_root():
    ''' Gives a list of users'''
    return await User.objects.all()

@app.get("/hello")
def hello():
    ''' Returns the hello message in json'''
    return {"message": "hello"}

@app.on_event("startup")
async def startup():
    if not database.is_connected:
        await database.connect()
    # Make a dummy user entry for now
    await User.objects.get_or_create(email="dev@dev.org")

@app.on_event("shutdown")
async def shutdown():
    if database.is_connected:
        await database.disconnect()
        