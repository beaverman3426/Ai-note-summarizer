from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize(input_data: TextInput):
    summary = summarizer(input_data.text, max_length=130, min_length=30, do_sample=False)
    return {"summary": summary[0]["summary_text"]}