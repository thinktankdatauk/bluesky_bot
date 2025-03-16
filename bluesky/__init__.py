import os

import pandas as pd

from .client import authenticate
from .fetch import download_bluesky_data

INPUT_DIR = "data"
INPUT_FILENAME = "thinktanks_list.csv"


def fetch_bluesky_data() -> None:
    """Download Bluesky data for list of handles"""

    client = authenticate()
    input_path = os.path.join(INPUT_DIR, INPUT_FILENAME)
    df_thinktanks = pd.read_csv(input_path)
    download_bluesky_data(client, df_thinktanks)
