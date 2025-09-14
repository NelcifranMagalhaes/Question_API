from pydantic import BaseModel

class QuestionCreate(BaseModel):
    label: str
    ordering: int

class QuestionResponse(QuestionCreate):
    id: str
    label: str
    ordering: int
