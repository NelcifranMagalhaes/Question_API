# 🏗️ Arquitetura do HappyTracker API

## Diagrama de Arquitetura

```mermaid
graph TB
    %% Camada de Apresentação/Interface
    subgraph "🌐 Camada de Apresentação"
        CLIENT[📱 Cliente/Frontend<br/>REST API Calls]
    end

    %% Camada de API
    subgraph "🚀 Camada de API - FastAPI"
        FASTAPI[⚡ FastAPI Application<br/>Port: 8000]
        
        subgraph "📍 Routers/Endpoints"
            USER_ROUTE[👤 User Routes<br/>/users]
            QUESTION_ROUTE[❓ Question Routes<br/>/questions]
            OPTION_ROUTE[📝 Option Routes<br/>/options]
            ANSWER_ROUTE[💬 Answer Routes<br/>/answers]
            METRICS_ROUTE[📊 Metrics Routes<br/>/answers/metrics]
        end
    end

    %% Camada de Validação
    subgraph "🔍 Camada de Validação - Pydantic Schemas"
        USER_SCHEMA[👤 User Schemas<br/>UserCreate, UserResponse]
        QUESTION_SCHEMA[❓ Question Schemas<br/>QuestionCreate, QuestionResponse]
        OPTION_SCHEMA[📝 Option Schemas<br/>OptionCreate, OptionResponse]
        ANSWER_SCHEMA[💬 Answer Schemas<br/>AnswerCreate, AnswerResponse]
        METRICS_SCHEMA[📊 Metrics Schemas<br/>QuestionMetrics, OptionMetric]
    end

    %% Camada de Lógica de Negócio
    subgraph "🧠 Camada de Modelos - Beanie ODM"
        USER_MODEL[👤 User Model<br/>name, email]
        QUESTION_MODEL[❓ Question Model<br/>label, ordering]
        OPTION_MODEL[📝 Option Model<br/>label, question_id]
        ANSWER_MODEL[💬 Answer Model<br/>user_id, question_id, option_id]
    end

    %% Camada de Dados
    subgraph "🗄️ Camada de Persistência"
        subgraph "🐳 Docker Container - MongoDB"
            MONGO[(🍃 MongoDB<br/>Port: 27017<br/>Database: happy_tracker_fast_api_db)]
            
            subgraph "📚 Collections"
                USERS_COLLECTION[👥 users]
                QUESTIONS_COLLECTION[❓ questions]
                OPTIONS_COLLECTION[📝 options]
                ANSWERS_COLLECTION[💬 answers]
            end
        end
    end

    %% Camada de Configuração
    subgraph "⚙️ Camada de Configuração"
        CONFIG[🔧 Configuration<br/>pydantic-settings]
        ENV[📄 Environment Variables<br/>.env file]
        DATABASE[🔌 Database Connection<br/>Motor + Beanie]
        SEED[🌱 Data Seeding<br/>seed.py]
    end

    %% Infraestrutura
    subgraph "🐳 Infraestrutura - Docker"
        DOCKER_COMPOSE[🐙 Docker Compose<br/>Orchestration]
        APP_CONTAINER[📦 FastAPI Container<br/>Python 3.11]
        MONGO_CONTAINER[📦 MongoDB Container<br/>Mongo:8]
        VOLUMES[💾 Persistent Volumes<br/>mongo_data]
    end

    %% Relações entre camadas
    CLIENT -->|HTTP Requests| FASTAPI
    
    FASTAPI --> USER_ROUTE
    FASTAPI --> QUESTION_ROUTE  
    FASTAPI --> OPTION_ROUTE
    FASTAPI --> ANSWER_ROUTE
    FASTAPI --> METRICS_ROUTE

    USER_ROUTE <--> USER_SCHEMA
    QUESTION_ROUTE <--> QUESTION_SCHEMA
    OPTION_ROUTE <--> OPTION_SCHEMA
    ANSWER_ROUTE <--> ANSWER_SCHEMA
    METRICS_ROUTE <--> METRICS_SCHEMA

    USER_SCHEMA <--> USER_MODEL
    QUESTION_SCHEMA <--> QUESTION_MODEL
    OPTION_SCHEMA <--> OPTION_MODEL
    ANSWER_SCHEMA <--> ANSWER_MODEL
    METRICS_SCHEMA --> QUESTION_MODEL
    METRICS_SCHEMA --> OPTION_MODEL
    METRICS_SCHEMA --> ANSWER_MODEL

    USER_MODEL <--> USERS_COLLECTION
    QUESTION_MODEL <--> QUESTIONS_COLLECTION
    OPTION_MODEL <--> OPTIONS_COLLECTION
    ANSWER_MODEL <--> ANSWERS_COLLECTION

    DATABASE --> MONGO
    CONFIG --> ENV
    CONFIG --> DATABASE
    
    DOCKER_COMPOSE --> APP_CONTAINER
    DOCKER_COMPOSE --> MONGO_CONTAINER
    APP_CONTAINER --> FASTAPI
    MONGO_CONTAINER --> MONGO
    VOLUMES --> MONGO

    SEED --> DATABASE
    SEED --> USER_MODEL
    SEED --> QUESTION_MODEL
    SEED --> OPTION_MODEL

    %% Estilos
    classDef apiLayer fill:#e1f5fe
    classDef schemaLayer fill:#f3e5f5
    classDef modelLayer fill:#e8f5e8
    classDef dataLayer fill:#fff3e0
    classDef configLayer fill:#fce4ec
    classDef infraLayer fill:#f1f8e9

    class CLIENT,FASTAPI,USER_ROUTE,QUESTION_ROUTE,OPTION_ROUTE,ANSWER_ROUTE,METRICS_ROUTE apiLayer
    class USER_SCHEMA,QUESTION_SCHEMA,OPTION_SCHEMA,ANSWER_SCHEMA,METRICS_SCHEMA schemaLayer
    class USER_MODEL,QUESTION_MODEL,OPTION_MODEL,ANSWER_MODEL modelLayer
    class MONGO,USERS_COLLECTION,QUESTIONS_COLLECTION,OPTIONS_COLLECTION,ANSWERS_COLLECTION dataLayer
    class CONFIG,ENV,DATABASE,SEED configLayer
    class DOCKER_COMPOSE,APP_CONTAINER,MONGO_CONTAINER,VOLUMES infraLayer
```

## 📋 Resumo da Arquitetura

### 🎯 Padrão Arquitetural
**Clean Architecture** + **Domain-Driven Design**

### 🏗️ Camadas da Aplicação

1. **🌐 Camada de Apresentação**
   - Interface REST API via FastAPI
   - Documentação automática (Swagger/OpenAPI)

2. **📍 Camada de Rotas/Controllers**
   - 4 routers principais: Users, Questions, Options, Answers
   - Endpoints especializados para métricas e análises

3. **🔍 Camada de Validação**
   - Schemas Pydantic para validação de entrada/saída
   - Tipagem forte e validação automática

4. **🧠 Camada de Modelos/Domínio**
   - Models Beanie (ODM para MongoDB)
   - Relacionamentos entre entidades

5. **🗄️ Camada de Persistência**
   - MongoDB como banco de dados NoSQL
   - Collections organizadas por domínio

### 🔗 Relacionamentos Entre Entidades

```
User (1) ←→ (N) Answer (N) ←→ (1) Question
                      ↓
                 (N) ←→ (1) Option
```

### 🚀 Stack Tecnológica

- **Framework**: FastAPI + Uvicorn
- **ODM**: Beanie (sobre Motor/PyMongo)
- **Banco**: MongoDB 8
- **Validação**: Pydantic
- **Containerização**: Docker + Docker Compose
- **Linguagem**: Python 3.11

### 📊 Funcionalidades Principais

- ✅ **CRUD** completo para Users, Questions, Options, Answers
- ✅ **Métricas avançadas** de respostas e engajamento
- ✅ **Sistema de logs** para auditoria
- ✅ **Seeding automático** de dados iniciais
- ✅ **Relacionamentos** complexos entre entidades

### 🎯 Endpoints da API

#### 👤 Users
- `POST /users` - Criar usuário
- `GET /users` - Listar usuários
- `GET /users/{user_id}` - Buscar usuário específico

#### ❓ Questions
- `POST /questions` - Criar questão
- `GET /questions` - Listar questões (ordenadas)
- `GET /questions/{question_id}` - Buscar questão com opções

#### 📝 Options
- `POST /options` - Criar opção
- `GET /options/by-question/{question_id}` - Listar opções por questão

#### 💬 Answers
- `POST /answers` - Criar resposta
- `GET /answers` - Listar todas as respostas
- `GET /answers/by-user/{user_id}` - Buscar respostas por usuário

#### 📊 Metrics
- `GET /answers/metrics/all` - Métricas de todas as questões com respostas
- Filtra apenas questões e opções que receberam respostas

### 🐳 Como Executar

```bash
# Subir containers
docker compose up -d

# Ver logs
docker compose logs -f

# Parar containers
docker compose down
```

### 📖 Acesso à Documentação
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc