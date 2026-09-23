from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from db.connection import Base


class Voter(Base):
    __tablename__ = "voter"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100),nullable=False)
    email = Column(String(150),unique=True,nullable=False,index=True)
    has_voted = Column(Boolean,default=False,nullable=False)
    votes = relationship("Vote",back_populates="voter")