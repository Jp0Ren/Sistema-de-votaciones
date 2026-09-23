from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connection import get_db
from models.candidate import Candidate
from models.voter import Voter
from schemas.candidate import CandidateResponse, CandidateCreate

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"]
)


@router.post(
    "",
    response_model=CandidateResponse, 
    status_code=201
)
def create_candidate(
    data: CandidateCreate,
    db: Session = Depends(get_db)
):

    existing_voter = (
        db.query(Voter)
        .filter(Voter.name == data.name)
        .first()
    )

    if existing_voter:
        raise HTTPException(
            status_code=409,
            detail="This person is already registered as voter"
        )

    candidate = Candidate(
        name=data.name,
        party=data.party
    )

    db.add(candidate)
    db.commit()
    db.refresh(candidate)

    return candidate


@router.get(
    "",
    response_model=list[CandidateResponse]
)
def get_candidates(
    db: Session = Depends(get_db)
):

    return db.query(Candidate).all()