# %%
import os

from atproto import Client
from atproto_client.models.app.bsky.actor.defs import ProfileViewDetailed
import pandas as pd

BLUESKY_USERNAME = os.getenv("BLUESKY_USERNAME")
BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")

# %%
# Load thinktank data
df_thinktanks = pd.read_csv("../data/thinktanks_list.csv")

# %%
# Authenticate with API
client = Client()
client.login(BLUESKY_USERNAME, BLUESKY_APP_PASSWORD)


# %%
def get_bluesky_data(handle: str) -> ProfileViewDetailed:
    """Get data from Bluesky API for a given handle"""
    print(handle)
    data = client.get_profile(actor=handle)

    return {
        "did": data.did,
        "display_name": data.display_name,
        "followers_count": data.followers_count,
        "created_at": data.created_at,
        "posts_count": data.posts_count,
    }


# %%
# Get the list of think tanks
df_thinktanks_expanded = df_thinktanks.apply(
    lambda x: get_bluesky_data(x["handle"]),
    axis="columns",
    result_type="expand",
)

# %%
# Add column holding current date
df_thinktanks_expanded["date"] = pd.Timestamp.now().date()

# %%
# Save to JSON
df_thinktanks_expanded.to_json("../data/thinktanks_bluesky.json", orient="records")
