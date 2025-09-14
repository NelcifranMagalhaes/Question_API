from fastapi import FastAPI
from app.database import init_db
from app.routes import user, question, option, answer

app = FastAPI(title="HappyTracker API", version="1.0.0")

@app.on_event("startup")
async def on_startup():
    await init_db()

# Registrar rotas
app.include_router(user.router)
app.include_router(question.router)
app.include_router(option.router)
app.include_router(answer.router)
