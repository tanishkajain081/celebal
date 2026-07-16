from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question_text = Column(String, nullable=False)
    category = Column(String, nullable=True)

    choices = relationship(
        "Choice",
        back_populates="question",
        cascade="all, delete"
    )


class Choice(Base):
    __tablename__ = "choices"

    id = Column(Integer, primary_key=True, index=True)
    choice_text = Column(String, nullable=False)
    is_correct = Column(Boolean, default=False)

    question_id = Column(
        Integer,
        ForeignKey("questions.id")
    )

    question = relationship(
        "Question",
        back_populates="choices"
    )