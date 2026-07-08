from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import uvicorn

# Gemini Client
client = genai.Client(api_key="AQ.Ab8RN6LkAuZCn7VbdZtaPMnEmo3Of5xrxPSYhzJFKiW_6ALOnQ")

# FastAPI App
app = FastAPI()

# Request Model
class ChatRequest(BaseModel):
    message: str

# Home Endpoint
@app.get("/")
def home():
    return {"message": "Gemini AI Backend is Running"}

# Chat Endpoint
@app.post("/chat")
def chat(request: ChatRequest):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.message
    )

    return {
        "question": request.message,
        "answer": response.text
    }

# Run Server
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
