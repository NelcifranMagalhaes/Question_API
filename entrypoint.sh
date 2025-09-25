#!/bin/sh
# Espera o Mongo estar acessível antes de rodar seeds
echo "Aguardando o MongoDB..."
sleep 5

echo "Rodando seeds..."
python app/seed.py || echo "Seeds já aplicados ou erro ignorado"

echo "Iniciando API..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
