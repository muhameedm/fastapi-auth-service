# FastAPI Auth Service

Small, production-ish FastAPI service with user registration & JWT login.

[![CI](https://github.com/muhameedm/fastapi-auth-service/actions/workflows/ci.yml/badge.svg)](https://github.com/muhameedm/fastapi-auth-service/actions)

## Stack
- FastAPI, Pydantic v2
- Postgres + SQLAlchemy + Alembic
- Docker / docker-compose
- pytest, ruff, black, isort
- GitHub Actions (lint + tests)

## Quick start (Docker)
```bash
cp .env.example .env
docker compose up --build
# Open http://localhost:8000/docs