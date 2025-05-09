import os
from typing import Optional

from atproto import Client
from atproto_client.exceptions import BadRequestError
import pandas as pd

OUTPUT_DIR = "data"
OUTPUT_FILENAME = "follower_counts.csv"


class BlueskyFetcher:
    """Handles fetching of data from Bluesky API"""

    def __init__(self, client: Client):
        self.client = client
        self.output_dir = OUTPUT_DIR
        self.output_filename = OUTPUT_FILENAME

    def download_bluesky_data(self, df_input: pd.DataFrame) -> pd.DataFrame:
        """Retrieve Bluesky data for rows of a df and save to CSV"""
        results = df_input.apply(
            lambda x: self.get_bluesky_profile(x["did"], x["handle"]),
            axis="columns",
            result_type="expand",
        )

        df_input_edited = results[
            [
                "display_name",
                "handle",
                "did",
            ]
        ]
        df_followers = results

        # Add current date
        df_followers["date"] = pd.Timestamp.now().date()

        # Save to CSV
        os.makedirs(self.output_dir, exist_ok=True)
        output_path = os.path.join(self.output_dir, self.output_filename)
        df_followers.to_csv(
            output_path,
            index=False,
            mode="a",
            header=not os.path.exists(output_path),
        )
        print(f"Follower data saved at {output_path}")

        return df_input_edited

    def get_bluesky_profile(self, did: Optional[str], handle: Optional[str]) -> dict:
        """Get data from Bluesky API for a given identifier (did) or handle"""
        if did is None and handle is None:
            raise ValueError("Either handle or did must be provided.")

        try:
            data = self.client.get_profile(actor=did if not pd.isna(did) else handle)
        except BadRequestError as e:
            print(
                f"Error fetching data for {handle} (did:{did}): {e}"  # noqa: E231, E501 https://github.com/PyCQA/pycodestyle/issues/1241
            )
            return {
                "display_name": None,
                "handle": None,
                "did": None,
                "created_at": None,
                "posts_count": None,
                "followers_count": None,
            }

        return {
            "display_name": data.display_name,
            "handle": data.handle,
            "did": data.did,
            "created_at": data.created_at,
            "posts_count": data.posts_count,
            "followers_count": data.followers_count,
        }
