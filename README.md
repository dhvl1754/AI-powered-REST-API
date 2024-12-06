# AI-powered-REST-API

An AI-powered REST API built using FastAPI and Hugging Face Transformers to provide intelligent customer support. The API supports real-time question-answering, feedback collection, and query logging for monitoring and improvement.

---

## Features

### 1. Health Check Endpoint
- **Endpoint**: `/health`
- **Method**: `GET`
- **Description**: Verifies that the API is running and operational.
- **Request Body**: None
- **Response**:
  ```json
  {
      "status": "running"
  }

### 2. Question Answering Endpoint
- **Endpoint**: `/answer`
- **Method**: `POST`
- **Description**: Takes a user question and context, processes it using a pre-trained AI model, and returns the answer with a confidence score. This endpoint originally used the distilbert-base-uncased-distilled-squad model, which gave a confidence level of 0.52. To improve performance, we switched to the bert-large-uncased-whole-word-masking-finetuned-squad model, increasing the confidence level to 0.72 for the same input.

#### - **Request Body**: 
```json
{
    "question": "What are the store hours?",
    "context": "Our store is open from 9 AM to 9 PM every day."
}
#### - **Response**:
  ```json
  {
    "question": "What are the store hours?",
    "answer": "9 AM to 9 PM",
    "confidence": 0.73
  }

### 3. Feedback Collection Endpoint
- **Endpoint**: `/feedback`
- **Method**: `POST`
- **Description**: Collects user feedback on the model's responses, storing it for future analysis and improvements.
- **Request Body**: 
```json
{
    "query_id": 1,
    "rating": 4,
    "comments": "The response was accurate."
}
- **Response**:
  ```json
  {
    "message": "Feedback submitted successfully"
  }


