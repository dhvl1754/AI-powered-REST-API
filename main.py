from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.exceptions import HTTPException
import sqlite3

app = FastAPI()

# Load the pre-trained AI model
# qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")


def log_query(question, context, answer, confidence):
    conn = sqlite3.connect("queries.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO queries (question, context, answer, confidence)
        VALUES (?, ?, ?, ?)
    """, (question, context, answer, confidence))
    conn.commit()
    conn.close()


class Query(BaseModel):
    question: str
    context: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI-powered REST API!"}

@app.get("/health")
def health_check():
    return {"status": "running"}

# @app.post("/answer")
# def get_answer(query: Query):
#     result = qa_pipeline(question=query.question, context=query.context)
#     log_query(query.question, query.context, result["answer"], result["score"])  # Log the query
#     return {
#         "question": query.question,
#         "answer": result["answer"],
#         "confidence": result["score"]
#     }

class Feedback(BaseModel):
    query_id: int
    rating: int
    comments: str = None

@app.post("/feedback")
def submit_feedback(feedback: Feedback):
    if feedback.rating < 1 or feedback.rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
    conn = sqlite3.connect("queries.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_id INTEGER NOT NULL,
            rating INTEGER NOT NULL,
            comments TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("""
        INSERT INTO feedback (query_id, rating, comments)
        VALUES (?, ?, ?)
    """, (feedback.query_id, feedback.rating, feedback.comments))
    conn.commit()
    conn.close()
    return {"message": "Feedback submitted successfully"}



@app.post("/answer")
def get_answer(query: Query):
    if not query.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    if not query.context.strip():
        raise HTTPException(status_code=400, detail="Context cannot be empty")
    result = qa_pipeline(question=query.question, context=query.context)
    log_query(query.question, query.context, result["answer"], result["score"])
    return {
        "question": query.question,
        "answer": result["answer"],
        "confidence": result["score"]
    }
