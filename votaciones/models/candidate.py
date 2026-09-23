from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.connection import Base


class Candidate(Base):
    __tablename__ = "candidate"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    party = Column(String(100), nullable=True)
    votes = Column(Integer, nullable=False, default=0)
    vote_records = relationship("Vote",back_populates="candidate")