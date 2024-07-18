
from fastapi  import FastAPI
from todo import todo_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict :
    return { "message" : "Hello World",
             "message1" : "그러니까"}

app.include_router(todo_router)
