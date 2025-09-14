from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
    user_data = user.model_dump()
    user_doc = User(**user_data)
    await user_doc.insert()
    return UserResponse(id=str(user_doc.id), **user_data)

@router.get("/", response_model=list[UserResponse])
async def list_users():
    users = await User.find_all().to_list()
    return [
        UserResponse(id=str(u.id), name=u.name, email=u.email)
        for u in users
    ]

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: str):
    try:
        uid = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user_id")

    user = await User.get(uid)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(id=str(user.id), name=user.name, email=user.email)
