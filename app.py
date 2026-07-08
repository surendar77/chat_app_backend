import gradio as gr
import requests

FASTAPI_URL = "http://127.0.0.1:8000/chat"

def chat(message):
    response = requests.post(
        FASTAPI_URL,
        json={"message": message}
    )

    if response.status_code == 200:
        return response.json()["answer"]
    else:
        return "Error connecting to FastAPI"

demo = gr.Interface(
    fn=chat,
    inputs=gr.Textbox(
        label="Ask Gemini",
        placeholder="Type your question..."
    ),
    outputs=gr.Textbox(label="Gemini Response"),
    title="Gemini AI Chatbot",
    description="Gradio + FastAPI + Gemini"
)

demo.launch()
