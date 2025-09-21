from beanie import Document
from pydantic import Field

class User(Document):
    name: str = Field(..., max_length=100)
    email: str
    password_hash: str =Field(..., max_length=100)  

    class Settings:
        name = "users"
