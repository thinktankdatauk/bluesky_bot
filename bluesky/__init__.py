import os

import pandas as pd

from .client import authenticate
from .fetch import BlueskyFetcher

INPUT_DIR = "data"
INPUT_FILENAME = "thinktanks_list.csv"


def fetch_bluesky_data() -> None:
    """Download Bluesky data for list of handles"""
    client = authenticate()
    fetcher = BlueskyFetcher(client)
    input_path = os.path.join(INPUT_DIR, INPUT_FILENAME)
    df_thinktanks = pd.read_csv(input_path)
    df_thinktanks_edited = fetcher.download_bluesky_data(df_thinktanks)
    if not df_thinktanks.equals(df_thinktanks_edited):
        df_thinktanks_edited.to_csv(input_path, index=False)
        print(f"Updated input data saved at {input_path}")
