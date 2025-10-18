
.PHONY: fmt lint test run migrate revision

fmt:
	black .
	isort .

lint:
	ruff check .

test:
	pytest -q

run:
	uvicorn app.main:app --reload

migrate:
	alembic upgrade head

revision:
	alembic revision --autogenerate -m "$(msg)"
