from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.models.question import Question
from app.schemas.question import QuestionCreate, QuestionResponse

router = APIRouter(prefix="/questions", tags=["questions"])

@router.post("/", response_model=QuestionResponse)
async def create_question(q: QuestionCreate):
    q_doc = Question(**q.model_dump())
    await q_doc.insert()
    return QuestionResponse(id=str(q_doc.id), **q.model_dump())

@router.get("/", response_model=list[QuestionResponse])
async def list_questions():
    questions = await Question.find_all().sort("ordering").to_list()
    return [QuestionResponse(id=str(q.id), label=q.label, ordering=q.ordering) for q in questions]

@router.get("/{question_id}", response_model=QuestionResponse)
async def get_question(question_id: str):
    try:
        qid = ObjectId(question_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid question_id")

    question = await Question.get(qid)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return QuestionResponse(id=str(question.id), label=question.label, ordering=question.ordering)
