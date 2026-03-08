from fastapi import FastAPI
from agent.agent import process_request

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Voice AI Agent Running"}

@app.post("/chat")
def chat(text: str):
    response = process_request(text)
    return {"response": response}