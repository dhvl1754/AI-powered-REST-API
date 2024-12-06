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

### Endpoint
`/answer`

### Method
`POST`

### Description
Takes a user question and context, processes it using a pre-trained AI model, and returns the answer with a confidence score.

### Request Body
```json
{
    "question": "What are the store hours?",
    "context": "Our store is open from 9 AM to 9 PM every day."
}


