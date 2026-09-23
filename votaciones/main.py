from fastapi import FastAPI
from db.connection import Base, engine
from routes import voter
from routes import candidate
from routes import vote


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Voting System API",
    description="REST API for managing a voting system",
    version="1.0.0"
)


app.include_router(
    voter.router
)

app.include_router(
    candidate.router
)

app.include_router(
    vote.router
)


@app.get("/")
def root():
    return {
        "message": "Voting System API",
        "version": "1.0.0"
    }