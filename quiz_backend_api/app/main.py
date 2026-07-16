from fastapi import FastAPI
from app.routers import questions, choices
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)
app = FastAPI(
    title="Quiz Backend Management API",
    description="REST API for managing quiz questions and choices",
    version="1.0.0"
)
app.include_router(questions.router)
app.include_router(choices.router)
@app.get("/")
def home():
    return {
        "message": "Welcome to the Quiz Backend Management API!"
    }