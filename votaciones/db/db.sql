create DATABASE voting;
use voting;

CREATE TABLE voter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    has_voted BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE candidate (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    party VARCHAR(100) NULL,
    votes INT NOT NULL DEFAULT 0
);

CREATE TABLE vote (
    id INT AUTO_INCREMENT PRIMARY KEY,
    voter_id INT NOT NULL,
    candidate_id INT NOT NULL,

    CONSTRAINT fk_vote_voter
        FOREIGN KEY (voter_id)
        REFERENCES voter(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT fk_vote_candidate
        FOREIGN KEY (candidate_id)
        REFERENCES candidate(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,

    CONSTRAINT uq_voter_vote
        UNIQUE (voter_id)
);