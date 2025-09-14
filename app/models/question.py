from beanie import Document
from pydantic import Field

class Question(Document):
    label: str = Field(..., max_length=255)
    ordering: int

    class Settings:
        name = "questions"
