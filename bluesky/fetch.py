import os

from atproto import Client
from atproto_client.models.app.bsky.actor.defs import ProfileViewDetailed
import pandas as pd

OUTPUT_DIR = "data"
OUTPUT_FILENAME = "thinktanks_bluesky_data.csv"


def get_bluesky_profile(client: Client, handle: str) -> ProfileViewDetailed:
    """Get data from Bluesky API for a given handle"""
    data = client.get_profile(actor=handle)

    return {
        "did": data.did,
        "display_name": data.display_name,
        "created_at": data.created_at,
        "posts_count": data.posts_count,
        "followers_count": data.followers_count,
    }


def download_bluesky_data(
    client: Client,
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Retrieve Bluesky data for rows of a df and save to CSV"""

    df[[
        "did",
        "display_name",
        "created_at",
        "posts_count",
        "followers_count",
    ]] = df.apply(
        lambda x: get_bluesky_profile(client, x["handle"]),
        axis="columns",
        result_type="expand",
    )

    # Add current date
    df["date"] = pd.Timestamp.now().date()

    # Save to CSV
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    df.to_csv(
        output_path,
        index=False,
        mode="a",
    )
    print(f"Data saved at {output_path}")
