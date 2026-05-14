from pydantic import BaseModel
from typing import List

class NumbersRequest(BaseModel):
    numbers: List[float]