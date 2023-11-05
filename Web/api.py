
from fastapi  import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict :
    return { "message" : "Hello World",
             "message1" : "그러니까"}
