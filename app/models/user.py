from beanie import Document
from pydantic import Field

class User(Document):
    name: str = Field(..., max_length=100)
    email: str

    class Settings:
        name = "users"
