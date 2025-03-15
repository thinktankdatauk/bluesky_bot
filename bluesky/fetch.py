import os

from atproto import Client
from atproto_client.models.app.bsky.actor.defs import ProfileViewDetailed
import pandas as pd

OUTPUT_DIR = "data"
OUTPUT_FILENAME = "thinktanks_bluesky.json"


def call_bluesky_api(client: Client, handle: str) -> ProfileViewDetailed:
    """Get data from Bluesky API for a given handle"""
    data = client.get_profile(actor=handle)

    return {
        "did": data.did,
        "display_name": data.display_name,
        "created_at": data.created_at,
        "posts_count": data.posts_count,
        "followers_count": data.followers_count,
    }


def get_bluesky_data(
    client: Client,
    df: pd.DataFrame,
) -> pd.DataFrame:
    """Get data from Bluesky API for a given handle"""

    df[[
        "did",
        "display_name",
        "created_at",
        "posts_count",
        "followers_count",
    ]] = df.apply(
        lambda x: call_bluesky_api(client, x["handle"]),
        axis="columns",
        result_type="expand",
    )

    # Add current date
    df["date"] = pd.Timestamp.now().date()

    # Save to JSON
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILENAME)
    df.to_json(
        output_path,
        orient="records",
    )
    print(f"Data saved at {output_path}")
