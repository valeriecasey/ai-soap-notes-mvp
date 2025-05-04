from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class SOAPNote(Base):
    __tablename__ = "soap_notes"

    id = Column(Integer, primary_key=True, index=True)
    subjective = Column(String, nullable=False)
    objective = Column(String, nullable=True)
    assessment = Column(String, nullable=True)
    plan = Column(String, nullable=True)

    class Config:
        orm_mode = True