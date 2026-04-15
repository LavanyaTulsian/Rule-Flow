from fastapi import FastAPI
from app.routers import rules

app = FastAPI()

app.include_router(rules.router, prefix="/rules", tags=["rules"])
