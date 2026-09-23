from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship
from db.connection import Base


class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer,primary_key=True,index=True)
    voter_id = Column(Integer,ForeignKey("voter.id"),nullable=False)
    candidate_id = Column(Integer,ForeignKey("candidate.id"),nullable=False)
    __table_args__ = (UniqueConstraint("voter_id",name="uq_vote_voter"),)
    voter = relationship("Voter",back_populates="votes")
    candidate = relationship("Candidate",back_populates="vote_records")