from beanie import Document
from beanie import PydanticObjectId
from pydantic import Field

class Answer(Document):
    
    user_id: PydanticObjectId
    question_id: PydanticObjectId
    option_id: PydanticObjectId

    class Settings:
        name = "answers"
