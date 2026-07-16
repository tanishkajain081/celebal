from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/questions",
    tags=["Questions"]
)


@router.post("/", response_model=schemas.QuestionResponse)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db, question)


@router.get("/", response_model=list[schemas.QuestionResponse])
def get_questions(db: Session = Depends(get_db)):
    return crud.get_questions(db)


@router.get("/{question_id}", response_model=schemas.QuestionResponse)
def get_question(question_id: int, db: Session = Depends(get_db)):
    question = crud.get_question(db, question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return question


@router.put("/{question_id}", response_model=schemas.QuestionResponse)
def update_question(
    question_id: int,
    question: schemas.QuestionCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_question(db, question_id, question)

    if not updated:
        raise HTTPException(status_code=404, detail="Question not found")

    return updated


@router.delete("/{question_id}")
def delete_question(question_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_question(db, question_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Question not found")

    return {"message": "Question deleted successfully"}