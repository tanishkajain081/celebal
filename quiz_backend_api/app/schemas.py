from pydantic import BaseModel
from typing import List, Optional


# ---------- Choice Schemas ----------

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


class ChoiceCreate(ChoiceBase):
    pass


class ChoiceResponse(ChoiceBase):
    id: int
    question_id: int

    class Config:
        from_attributes = True


# ---------- Question Schemas ----------

class QuestionBase(BaseModel):
    question_text: str
    category: Optional[str] = None


class QuestionCreate(QuestionBase):
    pass


class QuestionResponse(QuestionBase):
    id: int
    choices: List[ChoiceResponse] = []

    class Config:
        from_attributes = True