from fastapi import FastAPI
from ollama import Client
app = FastAPI()

client = Client(
    host=" "
)


@app.get("/")
def read_root():
    return {"The server is up and running":"OK"}