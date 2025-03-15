import os

import pandas as pd

from .client import authenticate
from .fetch import get_bluesky_data

INPUT_DIR = "data"
INPUT_FILENAME = "thinktanks_list.csv"


def fetch_bluesky_data():
    """Fetch data from Bluesky API"""

    client = authenticate()
    input_path = os.path.join(INPUT_DIR, INPUT_FILENAME)
    df_thinktanks = pd.read_csv(input_path)
    get_bluesky_data(client, df_thinktanks)

    return None
