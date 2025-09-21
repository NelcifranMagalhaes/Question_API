from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    password_hash: str

class UserResponse(BaseModel):
    id: str
    name: str
    email: str
