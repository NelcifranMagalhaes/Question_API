from pydantic import BaseModel
from typing import List
from .option import OptionResponse

class QuestionCreate(BaseModel):
    label: str
    ordering: int

class QuestionResponse(QuestionCreate):
    id: str
    label: str
    ordering: int
    options: List[OptionResponse] = []
