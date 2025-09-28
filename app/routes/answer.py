from bson import ObjectId
from fastapi import APIRouter, HTTPException
from app.models.answer import Answer
from app.models.question import Question
from app.models.option import Option
from app.schemas.answer import AnswerCreate, AnswerResponse, QuestionMetrics, OptionMetric
import logging
from collections import Counter

router = APIRouter(prefix="/answers", tags=["answers"])

@router.post("", response_model=AnswerResponse)
async def create_answer(ans: AnswerCreate):
    logging.info(f"Criando resposta para usuário {ans.user_id}, questão {ans.question_id}")
    
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

@router.get("", response_model=list[AnswerResponse])
async def list_answers():
    answers = await Answer.find_all().to_list()
    return [
        AnswerResponse(
            id=str(a.id),
            user_id=str(a.user_id),
            question_id=str(a.question_id),
            option_id=str(a.option_id),
        )
        for a in answers
    ]

@router.get("/metrics/all", response_model=list[QuestionMetrics])
async def get_all_metrics():
    """
    Retorna métricas apenas das questões que tiveram ao menos uma resposta
    """
    logging.info("Buscando métricas de questões com respostas")
    
    # Buscar todas as respostas para identificar quais questões têm respostas
    all_answers = await Answer.find_all().to_list()
    
    # Obter IDs únicos das questões que têm respostas
    question_ids_with_answers = list(set(answer.question_id for answer in all_answers))
    
    if not question_ids_with_answers:
        logging.info("Nenhuma questão com respostas encontrada")
        return []
    
    metrics_list = []
    
    for question_id in question_ids_with_answers:
        question = await Question.get(question_id)
        if not question:
            continue
        
        answers = await Answer.find(Answer.question_id == question_id).to_list()
        
        option_counts = Counter(str(answer.option_id) for answer in answers)
        
        options = await Option.find(Option.question_id == question_id).to_list()
        
        option_metrics = []
        total_options = len(options)
        for option in options:
            count = option_counts.get(str(option.id), 0)
            if count > 0:
                option_metrics.append(
                    OptionMetric(
                        option_id=str(option.id),
                        option_label=option.label,
                        count=count
                    )
                )
        
        logging.debug(f"Questão {question.label}: {len(option_metrics)}/{total_options} opções com respostas")
        
        metrics_list.append(
            QuestionMetrics(
                question_id=str(question.id),
                question_label=question.label,
                total_responses=len(answers),
                options=option_metrics
            )
        )
    
    logging.info(f"Retornando métricas de {len(metrics_list)} questões com respostas")
    return metrics_list
