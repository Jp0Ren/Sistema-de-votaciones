from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connection import get_db
from models.candidate import Candidate
from models.voter import Voter
from models.vote import Vote    
from schemas.vote import VoteCreate, VoteResponse 
from services.statistics import generate_statistics,generate_votes_chart


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]
)


@router.post(
    "",
    response_model=VoteResponse,
    status_code=201
)
def create_vote(
    data: VoteCreate,
    db: Session = Depends(get_db)
):

    voter = (
        db.query(Voter)
        .filter(Voter.id == data.voter_id)
        .with_for_update()
        .first()
    )

    if not voter:
        raise HTTPException(
            status_code=404,
            detail="Voter not found"
        )

    candidate = (
        db.query(Candidate)
        .filter(Candidate.id == data.candidate_id)
        .first()
    )

    if not candidate:
        raise HTTPException(
            status_code=404,
            detail="Candidate not found"
        )

    if voter.has_voted:
        raise HTTPException(
            status_code=409,
            detail="Voter has already voted"
        )

    vote = Vote(
        voter_id=voter.id,
        candidate_id=candidate.id
    )

    voter.has_voted = True
    candidate.votes += 1

    db.add(vote)

    try:
        db.commit()
        db.refresh(vote)

    except Exception:
        db.rollback()

        raise HTTPException(
            status_code=409,
            detail="Vote could not be registered"
        )

    return vote

@router.get("/statistics")
def get_statistics(db: Session = Depends(get_db)):

    candidates = db.query(Candidate).all()

    df, total_votes = generate_statistics(candidates)

    generate_votes_chart(df)

    return {
        "total_votes": int(total_votes),
        "total_voters_who_voted": int(total_votes),
        "candidates": df.to_dict(orient="records")
    }
