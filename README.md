# AIKYN Core

Суверенная AI-платформа для локального запуска интеллектуальных агентов, обработки документов, OCR, RAG и orchestration-сценариев.

---

## Возможности

* LLM inference
* RAG (Retrieval-Augmented Generation)
* OCR обработка документов
* Vision inference
* Multi-agent orchestration
* API-first архитектура
* Benchmarking
* Локальное развертывание
* Поддержка внутреннего документооборота

---

## Архитектура

```text
Client
  ↓
API Gateway
  ↓
Agent Router
  ↓
Core / Growth Agents
  ↓
LLM / Vision / OCR
  ↓
RAG + Memory + Vector DB
```

---

## Структура проекта

```text
agents/       AI-агенты
api/          REST API
benchmarks/   тестирование и eval
docs/         документация
infra/        инфраструктурные конфиги
ocr/          OCR сервисы
ops/          deployment / scripts
rag/          retrieval pipeline
workers/      background tasks
```

---

## Требования

### Минимум

* Docker
* Docker Compose
* 32 GB RAM
* NVIDIA GPU (рекомендуется)

### Рекомендуется

* Ubuntu 22.04
* 64+ GB RAM
* RTX 3090 / RTX 4090
* CUDA 12+

---

## Быстрый старт

### 1. Клонирование

```bash
git clone https://github.com/sunbusinessbooks/aikyn.git
cd aikyn
```

---

### 2. Создание env

```bash
cp .env.example .env
```

Заполни:

* database credentials
* service urls
* model endpoints

---

### 3. Запуск инфраструктуры

```bash
docker compose up -d
```

---

### 4. Проверка

API:

```bash
http://localhost:8000
```

Healthcheck:

```bash
curl http://localhost:8000/health
```

---

## Конфигурация

### Основные параметры

### API

```env
APP_ENV=development
APP_HOST=0.0.0.0
APP_PORT=8000
```

### PostgreSQL

```env
POSTGRES_DB=aikyn
POSTGRES_USER=aikyn
POSTGRES_PASSWORD=change_me
```

### Redis

```env
REDIS_HOST=redis
REDIS_PORT=6379
```

### Qdrant

```env
QDRANT_HOST=qdrant
QDRANT_PORT=6333
```

---

## Запуск сервисов

### API

```bash
python -m api.main
```

### Workers

```bash
python -m workers.main
```

### OCR

```bash
python -m ocr.main
```

---

## Работа с документами

Добавление документов:

```bash
python rag/ingest.py
```

Индексация:

```bash
python rag/index.py
```

---

## Агенты

### Core

Внутренний операционный агент:

* работа с документами
* ответы по регламентам
* поддержка команды

---

### Growth

Аналитический агент:

* гипотезы роста
* стратегия
* анализ эффективности

---

## Benchmarks

Запуск:

```bash
python benchmarks/run.py
```

Метрики:

* latency
* retrieval accuracy
* response quality
* token throughput

---

## Разработка

Форматирование:

```bash
black .
```

Проверка:

```bash
pytest
```

---

## Roadmap

### MVP

* API
* базовый router
* LLM интеграция
* Telegram interface

### Phase 2

* memory layer
* advanced RAG
* OCR pipeline

### Phase 3

* multi-agent collaboration
* autonomous workflows
* regional sovereign deployment

---

## Безопасность

Никогда не коммить:

* `.env`
* production credentials
* API keys

---

## Лицензия

Private / Internal

---

## Миссия

AIKYN Core создаётся как суверенная интеллектуальная платформа для построения локальных AI-систем нового поколения.
