from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.models.option import Option
from app.schemas.option import OptionCreate, OptionResponse

router = APIRouter(prefix="/options", tags=["options"])

@router.post("/", response_model=OptionResponse)
async def create_option(opt: OptionCreate):
    try:
        qid = ObjectId(opt.question_id)   # 👈 valida id
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid question_id")

    opt_doc = Option(label=opt.label, question_id=qid)
    await opt_doc.insert()
    return OptionResponse(id=str(opt_doc.id), label=opt_doc.label, question_id=str(opt_doc.question_id))

@router.get("/by-question/{question_id}", response_model=list[OptionResponse])
async def list_options_by_question(question_id: str):
    try:
        qid = ObjectId(question_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid question_id")

    options = await Option.find(Option.question_id == qid).to_list()
    return [
        OptionResponse(id=str(o.id), label=o.label, question_id=str(o.question_id))
        for o in options
    ]
