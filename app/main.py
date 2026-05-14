from fastapi import FastAPI, Depends
from app.models import NumbersRequest
from app.auth import verify_api_key

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Sequential Sum API is running"
    }

@app.post("/sum")
def sequential_sum(
    data: NumbersRequest,
    auth: None = Depends(verify_api_key)
):
    
    total = 0

    for number in data.numbers:
        total += number

    return {
        "numbers": data.numbers,
        "sum": total
    }