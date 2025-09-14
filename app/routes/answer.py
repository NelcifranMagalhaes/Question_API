from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.models.answer import Answer
from app.schemas.answer import AnswerCreate, AnswerResponse

router = APIRouter(prefix="/answers", tags=["answers"])

@router.post("/", response_model=AnswerResponse)
async def create_answer(ans: AnswerCreate):
    try:
        uid = ObjectId(ans.user_id)
        qid = ObjectId(ans.question_id)
        oid = ObjectId(ans.option_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    ans_doc = Answer(user_id=uid, question_id=qid, option_id=oid)
    await ans_doc.insert()
    return AnswerResponse(
        id=str(ans_doc.id),
        user_id=str(ans_doc.user_id),
        question_id=str(ans_doc.question_id),
        option_id=str(ans_doc.option_id),
    )

@router.get("/by-user/{user_id}", response_model=list[AnswerResponse])
async def list_answers_by_user(user_id: str):
    try:
        uid = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user_id")

    answers = await Answer.find(Answer.user_id == uid).to_list()
    return [
        AnswerResponse(
            id=str(a.id),
            user_id=str(a.user_id),
            question_id=str(a.question_id),
            option_id=str(a.option_id),
        )
        for a in answers
    ]
