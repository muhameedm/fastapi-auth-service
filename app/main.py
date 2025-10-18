from fastapi import FastAPI
from app.routers import health, users, auth, register

app = FastAPI(title="FastAPI Starter", version="0.1.0")

# Include Routers
app.include_router(health.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(auth.router)
app.include_router(register.router)