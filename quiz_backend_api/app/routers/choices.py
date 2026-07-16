from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/choices",
    tags=["Choices"]
)


@router.post("/{question_id}", response_model=schemas.ChoiceResponse)
def create_choice(
    question_id: int,
    choice: schemas.ChoiceCreate,
    db: Session = Depends(get_db)
):
    question = crud.get_question(db, question_id)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return crud.create_choice(db, choice, question_id)


@router.get("/", response_model=list[schemas.ChoiceResponse])
def get_choices(db: Session = Depends(get_db)):
    return crud.get_choices(db)


@router.get("/{choice_id}", response_model=schemas.ChoiceResponse)
def get_choice(choice_id: int, db: Session = Depends(get_db)):
    choice = crud.get_choice(db, choice_id)

    if not choice:
        raise HTTPException(status_code=404, detail="Choice not found")

    return choice


@router.put("/{choice_id}", response_model=schemas.ChoiceResponse)
def update_choice(
    choice_id: int,
    choice: schemas.ChoiceCreate,
    db: Session = Depends(get_db)
):
    updated = crud.update_choice(db, choice_id, choice)

    if not updated:
        raise HTTPException(status_code=404, detail="Choice not found")

    return updated


@router.delete("/{choice_id}")
def delete_choice(choice_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_choice(db, choice_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Choice not found")

    return {"message": "Choice deleted successfully"}