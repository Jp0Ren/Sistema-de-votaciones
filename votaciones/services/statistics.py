import pandas as pd
import matplotlib.pyplot as plt


def generate_statistics(candidates):

    data = [
        {
            "candidate": candidate.name,
            "votes": candidate.votes
        }
        for candidate in candidates
    ]

    df = pd.DataFrame(data)

    total_votes = df["votes"].sum()

    if total_votes > 0:
        df["percentage"] = (
            df["votes"] / total_votes * 100
        ).round(2)
    else:
        df["percentage"] = 0

    return df, total_votes


def generate_votes_chart(df):

    ax = df.plot(
        x="candidate",
        y="votes",
        kind="bar",
        legend=False
    )

    ax.set_xlabel("Candidatos")
    ax.set_ylabel("Votos")
    ax.set_title("Resultados de la votación")

    plt.tight_layout()

    plt.savefig("reports/votes.png")

    plt.close()