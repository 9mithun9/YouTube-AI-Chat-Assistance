# backend/app.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from get_transcript_answer import get_transcript_and_answer

app = FastAPI()

# Enable CORS for all origins (adjust if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskRequest(BaseModel):
    video_id: str
    question: str

@app.post("/ask-question")
def ask_question(data: AskRequest):
    answer = get_transcript_and_answer(data.video_id, data.question)
    return {"answer": answer}
