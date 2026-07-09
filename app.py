from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import uvicorn

# Gemini Client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

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

