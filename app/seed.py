import sys
import os
import asyncio

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import init_db
from app.models.question import Question
from app.models.option import Option
from app.models.user import User
from app.models.answer import Answer


async def seed():
    await init_db()

    # limpa coleções para não duplicar
    await Question.delete_all()
    await Option.delete_all()
    await User.delete_all()
    await Answer.delete_all()

    # questions
    questions_data = [
        {"label": "Escolha o seu emoji de hoje!", "ordering": 1},
        {"label": "Como você se sente hoje?", "ordering": 2},
        {"label": "Como você avalia sua carga de trabalho?", "ordering": 3},
        {"label": "Sua carga de trabalho afeta sua qualidade de vida?", "ordering": 4},
        {"label": "Você trabalha além do seu horário regular?", "ordering": 5},
        {"label": "Você tem apresentado sintomas como insônia, irritabilidade ou cansaço extremo?", "ordering": 6},
        {"label": "Você sente que sua saúde mental prejudica sua produtividade no trabalho?", "ordering": 7},
        {"label": "Sinto que posso me comunicar abertamente com minha liderança.", "ordering": 8},
    ]

    inserted_questions = []
    for q in questions_data:
        q_doc = Question(**q)
        await q_doc.insert()
        inserted_questions.append(q_doc)

    # options
    options_map = {
        1: ["Triste", "Alegre", "Cansado", "Ansioso", "Medo", "Raiva"],
        2: ["Motivado", "Cansado", "Preocupado", "Estressado", "Animado", "Satisfeito"],
        3: ["Muito Leve", "Leve", "Média", "Alta", "Muito Alta"],
        4: ["Não", "Raramente", "Às vezes", "Frequentemente", "Sempre"],
        5: ["Não", "Raramente", "Às vezes", "Frequentemente", "Sempre"],
        6: ["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"],
        7: ["Nunca", "Raramente", "Às vezes", "Frequentemente", "Sempre"],
        8: ["1", "2", "3", "4", "5"],
    }

    # users
    user_one = User(name="Worker1", email="worker1@example.com")
    user_two = User(name="Worker2", email="worker2@example.com")
    await user_one.insert()
    await user_two.insert()

    for idx, q_doc in enumerate(inserted_questions, start=1):
        for label in options_map[idx]:
            opt = Option(label=label, question_id=q_doc.id)
            await opt.insert()

    print("✅ Seed finalizado com sucesso!")


if __name__ == "__main__":
    asyncio.run(seed())
