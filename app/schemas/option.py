from pydantic import BaseModel

class OptionCreate(BaseModel):
    label: str
    question_id: str

class OptionResponse(OptionCreate):
    id: str
    label: str
    question_id: str