# %%
import pandas as pd

from .client import authenticate
from .fetch import get_bluesky_data


def fetch_bluesky_data():
    """Fetch data from Bluesky API"""

    client = authenticate()
    df_thinktanks = pd.read_csv("../data/thinktanks_list.csv")
    get_bluesky_data(client, df_thinktanks)

    return None
