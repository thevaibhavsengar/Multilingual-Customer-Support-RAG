from pydantic import BaseModel
from typing import List


class UploadResponse(BaseModel):
    message: str


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str
    sources: List[str]