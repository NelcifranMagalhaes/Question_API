from pydantic import BaseModel
from typing import List

class AnswerCreate(BaseModel):
    user_id: str
    question_id: str
    option_id: str

class AnswerResponse(AnswerCreate):
    id: str
    user_id: str
    question_id: str
    option_id: str

class OptionMetric(BaseModel):
    option_id: str
    option_label: str
    count: int

class QuestionMetrics(BaseModel):
    question_id: str
    question_label: str
    total_responses: int
    options: List[OptionMetric]
