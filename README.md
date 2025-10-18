
# FastAPI Starter (Production-ish, Student-Friendly)

A clean FastAPI template with:
- **PostgreSQL** + SQLAlchemy
- **Alembic** migrations
- **Docker / docker-compose**
- **pytest** tests
- **pre-commit** (black + ruff + isort)
- **GitHub Actions** CI (lint + tests)
- Health endpoint + Users CRUD example

## Quick Start (Docker)
```bash
cp .env.example .env
docker compose up --build
# App at http://localhost:8000  (Docs: /docs)
```

Run first migration and create tables:
```bash
docker compose run --rm app alembic upgrade head
```

## Local (without Docker)
```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

## Makefile (handy)
```bash
make fmt       # format (black + isort)
make lint      # ruff check
make test      # run pytest
make run       # run uvicorn
make migrate   # alembic upgrade head
make revision  # create migration: make revision msg="add users"
```

## Project Layout
```
app/
  main.py
  core/config.py
  db/session.py
  db/base.py
  models.py
  schemas.py
  routers/
    health.py
    users.py
alembic/
  env.py
  versions/
tests/
  test_health.py
  test_users.py
```

## Default credentials
Database reads from environment variables (see `.env.example`).

---

### Notes
- Tests use **SQLite (in-memory)** by overriding the DB dependency, independent of your Postgres.
- Replace/expand the `User` model and add more routers as you go.
- Keep CI green before pushing.
