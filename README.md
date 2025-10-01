# 🎯 HappyTracker API

> **API REST para coleta e análise de dados de bem-estar e satisfação no trabalho**

Uma solução completa para empresas monitorarem o bem-estar de seus colaboradores através de questionários personalizáveis e métricas em tempo real.

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)

## 🚀 Características Principais

- ✅ **API REST** completa com FastAPI
- ✅ **Sistema de questionários** flexível e customizável
- ✅ **Métricas avançadas** de engajamento e respostas
- ✅ **Banco NoSQL** MongoDB para alta performance
- ✅ **Containerização** com Docker
- ✅ **Documentação automática** Swagger/OpenAPI
- ✅ **Validação robusta** com Pydantic
- ✅ **Sistema de logs** para auditoria
- ✅ **Seeding automático** de dados iniciais

## 📋 Índice

- [🏗️ Arquitetura](#️-arquitetura)
- [🛠️ Tecnologias](#️-tecnologias)
- [⚡ Quick Start](#-quick-start)
- [📖 Documentação da API](#-documentação-da-api)
- [🔧 Configuração](#-configuração)
- [🎯 Endpoints](#-endpoints)
- [📊 Métricas e Analytics](#-métricas-e-analytics)
- [🧪 Desenvolvimento](#-desenvolvimento)
- [📚 Exemplos de Uso](#-exemplos-de-uso)
- [🤝 Contribuição](#-contribuição)

## 🏗️ Arquitetura

O projeto segue os princípios de **Clean Architecture** e **Domain-Driven Design**:

```
📱 Cliente/Frontend
    ↓ HTTP REST
🚀 FastAPI (Routers)
    ↓ Validação
🔍 Pydantic Schemas
    ↓ Lógica de Negócio  
🧠 Beanie Models (ODM)
    ↓ Persistência
🗄️ MongoDB Collections
```

Para ver o diagrama completo da arquitetura, consulte: [ARCHITECTURE.md](./ARCHITECTURE.md)

## 🛠️ Tecnologias

| Categoria | Tecnologia | Versão | Descrição |
|-----------|------------|--------|-----------|
| **Framework** | FastAPI | Latest | Framework web moderno e rápido |
| **Linguagem** | Python | 3.11 | Linguagem de programação |
| **Banco de Dados** | MongoDB | 8.0 | Banco NoSQL orientado a documentos |
| **ODM** | Beanie | Latest | Object Document Mapper para MongoDB |
| **Validação** | Pydantic | Latest | Validação de dados e serialização |
| **Containerização** | Docker | Latest | Containerização da aplicação |
| **Servidor ASGI** | Uvicorn | Latest | Servidor ASGI para FastAPI |

## ⚡ Quick Start

### Pré-requisitos

- 🐳 **Docker** e **Docker Compose**
- 🔧 **Git**

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/NelcifranMagalhaes/Question_API.git
cd Question_API
```

### 2️⃣ Configure as Variáveis de Ambiente

```bash
# O arquivo .env já está configurado com valores padrão
cat .env
```

### 3️⃣ Execute a Aplicação

```bash
# Subir todos os serviços
docker compose up -d

# Ver logs em tempo real
docker compose logs -f app
```

### 4️⃣ Acesse a API

- 🌐 **API Base**: http://localhost:8000
- 📖 **Documentação Swagger**: http://localhost:8000/docs
- 📚 **ReDoc**: http://localhost:8000/redoc

### 5️⃣ Teste a API

```bash
# Listar todas as questões
curl http://localhost:8000/questions

# Ver métricas
curl http://localhost:8000/answers/metrics/all
```

## 📖 Documentação da API

A API possui documentação automática gerada pelo FastAPI:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

## 🔧 Configuração

### Variáveis de Ambiente

| Variável | Descrição | Valor Padrão |
|----------|-----------|--------------|
| `MONGO_URI` | URI de conexão MongoDB | `mongodb://mongo:27017` |
| `MONGO_DB` | Nome do banco de dados | `happy_tracker_fast_api_db` |

### Estrutura de Arquivos

```
📁 Question_API/
├── 📁 app/                    # Código da aplicação
│   ├── 📁 models/            # Modelos Beanie (ODM)
│   ├── 📁 routes/            # Endpoints/Routers
│   ├── 📁 schemas/           # Schemas Pydantic
│   ├── 📄 main.py            # Aplicação principal
│   ├── 📄 database.py        # Configuração do banco
│   ├── 📄 config.py          # Configurações
│   └── 📄 seed.py            # Dados iniciais
├── 📄 docker-compose.yml     # Orquestração Docker
├── 📄 Dockerfile             # Imagem da aplicação
├── 📄 requirements.txt       # Dependências Python
├── 📄 .env                   # Variáveis de ambiente
├── 📄 ARCHITECTURE.md        # Diagrama de arquitetura
└── 📄 README.md              # Este arquivo
```

## 🎯 Endpoints

### 👤 Usuários (`/users`)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/users` | Criar novo usuário |
| `GET` | `/users` | Listar todos os usuários |
| `GET` | `/users/{user_id}` | Buscar usuário específico |

### ❓ Questões (`/questions`)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/questions` | Criar nova questão |
| `GET` | `/questions` | Listar questões ordenadas |
| `GET` | `/questions/{question_id}` | Buscar questão com opções |

### 📝 Opções (`/options`)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/options` | Criar nova opção |
| `GET` | `/options/by-question/{question_id}` | Listar opções por questão |

### 💬 Respostas (`/answers`)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/answers` | Criar nova resposta |
| `GET` | `/answers` | Listar todas as respostas |
| `GET` | `/answers/by-user/{user_id}` | Respostas por usuário |

### 📊 Métricas (`/answers/metrics`)

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/answers/metrics/all` | Métricas de todas as questões |

## 📊 Métricas e Analytics

### Funcionalidades de Análise

- 📈 **Contagem de respostas** por opção
- 🎯 **Filtros inteligentes** (apenas dados com engajamento)
- 📊 **Métricas agregadas** por questão
- 🔍 **Análise de participação** dos usuários

### Exemplo de Resposta de Métricas

```json
{
  "question_id": "64f8a123b456c789d012e345",
  "question_label": "Como você se sente hoje?",
  "total_responses": 25,
  "options": [
    {
      "option_id": "64f8a123b456c789d012e346",
      "option_label": "Motivado",
      "count": 15
    },
    {
      "option_id": "64f8a123b456c789d012e347", 
      "option_label": "Cansado",
      "count": 10
    }
  ]
}
```

## 🧪 Desenvolvimento

### Executar em Modo de Desenvolvimento

```bash
# Instalar dependências localmente
pip install -r requirements.txt

# Executar com reload automático
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Comandos Úteis

```bash
# Ver logs da aplicação
docker compose logs -f app

# Acessar container da aplicação
docker compose exec app bash

# Acessar MongoDB
docker compose exec mongo mongosh

# Parar todos os serviços
docker compose down

# Rebuild da aplicação
docker compose build --no-cache app
```

### Estrutura do Banco de Dados

```javascript
// Collection: users
{
  "_id": ObjectId,
  "name": "string",
  "email": "string"
}

// Collection: questions  
{
  "_id": ObjectId,
  "label": "string",
  "ordering": number
}

// Collection: options
{
  "_id": ObjectId,
  "label": "string", 
  "question_id": ObjectId
}

// Collection: answers
{
  "_id": ObjectId,
  "user_id": ObjectId,
  "question_id": ObjectId,
  "option_id": ObjectId
}
```

## 📚 Exemplos de Uso

### Criar um Usuário

```bash
curl -X POST "http://localhost:8000/users" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "João Silva",
    "email": "joao@empresa.com"
  }'
```

### Criar uma Questão

```bash
curl -X POST "http://localhost:8000/questions" \
  -H "Content-Type: application/json" \
  -d '{
    "label": "Como você avalia o clima organizacional?",
    "ordering": 1
  }'
```

### Registrar uma Resposta

```bash
curl -X POST "http://localhost:8000/answers" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "64f8a123b456c789d012e345",
    "question_id": "64f8a123b456c789d012e346", 
    "option_id": "64f8a123b456c789d012e347"
  }'
```

### Obter Métricas

```bash
curl "http://localhost:8000/answers/metrics/all"
```

## 🎯 Casos de Uso

### Para Empresas
- 📊 **Pesquisas de clima organizacional**
- 💼 **Avaliação de satisfação dos funcionários**  
- 🎯 **Monitoramento de bem-estar**
- 📈 **Análise de engajamento da equipe**

### Para RH
- 📋 **Questionários personalizáveis**
- 📊 **Dashboards de métricas**
- 🔍 **Análise de tendências**
- 📈 **Relatórios executivos**

## 🚨 Troubleshooting

### Problemas Comuns

#### Container não sobe
```bash
# Verificar se as portas estão livres
netstat -tulpn | grep :8000
netstat -tulpn | grep :27017

# Limpar containers antigos
docker system prune -f
```

#### Erro de conexão com MongoDB
```bash
# Verificar se o MongoDB está rodando
docker compose ps

# Ver logs do MongoDB
docker compose logs mongo
```

#### Erro 307 Redirect
- Certifique-se de fazer requisições para URLs sem barra final
- ✅ Correto: `POST /answers`
- ❌ Incorreto: `POST /answers/`

## 🤝 Contribuição

1. 🍴 **Fork** o projeto
2. 🌟 **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. 💾 **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. 📤 **Push** para a branch (`git push origin feature/AmazingFeature`)
5. 🔄 **Abra** um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Autores

- **Nelcifran Magalhães** - *Desenvolvimento inicial* - [@NelcifranMagalhaes](https://github.com/NelcifranMagalhaes)

## 🙏 Agradecimentos

- FastAPI pela excelente framework
- MongoDB pela robustez do banco de dados
- Beanie pelo ODM elegante e eficiente
- Docker pela simplicidade de deployment

---

<div align="center">

**[⬆ Voltar ao topo](#-happytracker-api)**

Feito com ❤️ para melhorar o bem-estar no trabalho

</div>