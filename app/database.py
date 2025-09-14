import motor.motor_asyncio
from beanie import init_beanie
from app.config import settings
from app.models.user import User
from app.models.question import Question
from app.models.option import Option
from app.models.answer import Answer

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
    database = client[settings.MONGO_DB]
    await init_beanie(database=database, document_models=[User, Question, Option, Answer])
