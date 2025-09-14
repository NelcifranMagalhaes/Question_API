from pydantic import BaseModel

class AnswerCreate(BaseModel):
    user_id: str
    question_id: str
    option_id: str

class AnswerResponse(AnswerCreate):
    id: str
    user_id: str
    question_id: str
    option_id: str
