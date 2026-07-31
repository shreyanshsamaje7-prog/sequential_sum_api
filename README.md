# Sequential Sum API

A secure RESTful API built with FastAPI that calculates the sequential sum of a list of numbers using API Key Authentication.

---

# Features

- FastAPI-based REST API
- POST `/sum` endpoint
- API Key Authentication
- JSON request/response
- Input validation using Pydantic
- Easy deployment

---

# Project Structure

```bash
sequential-sum-api/
│
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── models.py
│   └── config.py
│
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/sequential-sum-api.git
cd sequential-sum-api
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the root directory.

```env
API_KEY=mysecureapikey123
```

---

# Run the Server

```bash
uvicorn app.main:app --reload
```

Server URL:

```text
http://127.0.0.1:8000
```

---

# API Documentation

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoint

## POST `/sum`

Calculates the sequential sum of numbers.

---

# Request Headers

| Header | Value |
|---|---|
| Content-Type | application/json |
| X-API-KEY | your_api_key |

---

# Request Body

```json
{
  "numbers": [5, 10, 15]
}
```

---

# Success Response

```json
{
  "numbers": [5, 10, 15],
  "sum": 30
}
```

Status Code:

```text
200 OK
```

---

# Error Responses

## Invalid API Key

```json
{
  "detail": "Invalid API Key"
}
```

Status Code:

```text
401 Unauthorized
```

---

## Missing API Key

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["header", "x-api-key"],
      "msg": "Field required"
    }
  ]
}
```

Status Code:

```text
422 Unprocessable Entity
```

---

# Testing with curl

## Successful Request

```bash
curl -X POST "http://127.0.0.1:8000/sum" \
-H "Content-Type: application/json" \
-H "X-API-KEY: mysecureapikey123" \
-d "{\"numbers\":[5,10,15]}"
```

---

## Invalid API Key

```bash
curl -X POST "http://127.0.0.1:8000/sum" \
-H "Content-Type: application/json" \
-H "X-API-KEY: wrongkey123" \
-d "{\"numbers\":[5,10,15]}"
```

---

# Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv

---

# Deployment

Can be deployed on:

- Render
- Railway
- Heroku
- AWS
- Google Cloud

---

# Author

Shreyansh Samaje
like this it will work
