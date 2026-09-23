from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connection import get_db
from models.candidate import Candidate
from models.voter import Voter
from schemas.voter import VoterCreate, VoterResponse

router = APIRouter(
    prefix="/voters",
    tags=["Voters"]
)


@router.post(
    "",
    response_model=VoterResponse,
    status_code=201
)
def create_voter(
    data: VoterCreate,
    db: Session = Depends(get_db)
):

    existing_voter = (
        db.query(Voter)
        .filter(Voter.email == data.email)
        .first()
    )

    if existing_voter:
        raise HTTPException(
            status_code=409,
            detail="Email already registered as voter"
        )

    existing_candidate = (
        db.query(Candidate)
        .filter(Candidate.name == data.name)
        .first()
    )

    if existing_candidate:
        raise HTTPException(
            status_code=409,
            detail="This person is already registered as candidate"
        )

    voter = Voter(
        name=data.name,
        email=data.email
    )

    db.add(voter)
    db.commit()
    db.refresh(voter)

    return voter


@router.delete("/{voter_id}")
def delete_voter(
    voter_id: int,
    db: Session = Depends(get_db)
):

    voter = (
        db.query(Voter)
        .filter(Voter.id == voter_id)
        .first()
    )

    if not voter:
        raise HTTPException(
            status_code=404,
            detail="Voter not found"
        )

    if voter.has_voted:
        raise HTTPException(
            status_code=400,
            detail="A voter who has already voted cannot be deleted"
        )

    db.delete(voter)
    db.commit()

    return {
        "message": "Voter deleted successfully"
    }