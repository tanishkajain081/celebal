from sqlalchemy.orm import Session
from app import models, schemas


# -----------------------------
# Question CRUD
# -----------------------------

def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(
        question_text=question.question_text,
        category=question.category
    )

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


def get_questions(db: Session):
    return db.query(models.Question).all()


def get_question(db: Session, question_id: int):
    return (
        db.query(models.Question)
        .filter(models.Question.id == question_id)
        .first()
    )


def update_question(db: Session, question_id: int, question: schemas.QuestionCreate):
    db_question = get_question(db, question_id)

    if db_question:
        db_question.question_text = question.question_text
        db_question.category = question.category

        db.commit()
        db.refresh(db_question)

    return db_question


def delete_question(db: Session, question_id: int):
    db_question = get_question(db, question_id)

    if db_question:
        db.delete(db_question)
        db.commit()

    return db_question


# -----------------------------
# Choice CRUD
# -----------------------------

def create_choice(db: Session, choice: schemas.ChoiceCreate, question_id: int):
    db_choice = models.Choice(
        choice_text=choice.choice_text,
        is_correct=choice.is_correct,
        question_id=question_id
    )

    db.add(db_choice)
    db.commit()
    db.refresh(db_choice)

    return db_choice


def get_choices(db: Session):
    return db.query(models.Choice).all()


def get_choice(db: Session, choice_id: int):
    return (
        db.query(models.Choice)
        .filter(models.Choice.id == choice_id)
        .first()
    )


def update_choice(db: Session, choice_id: int, choice: schemas.ChoiceCreate):
    db_choice = get_choice(db, choice_id)

    if db_choice:
        db_choice.choice_text = choice.choice_text
        db_choice.is_correct = choice.is_correct

        db.commit()
        db.refresh(db_choice)

    return db_choice


def delete_choice(db: Session, choice_id: int):
    db_choice = get_choice(db, choice_id)

    if db_choice:
        db.delete(db_choice)
        db.commit()

    return db_choice