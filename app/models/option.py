from beanie import Document
from pydantic import Field
from beanie import PydanticObjectId

class Option(Document):
    label: str = Field(..., max_length=255)
    question_id: PydanticObjectId

    class Settings:
        name = "options"
