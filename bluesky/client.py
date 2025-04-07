import os

from atproto import Client
from dotenv import load_dotenv

load_dotenv()

BLUESKY_USERNAME = os.getenv("BLUESKY_USERNAME")
BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")


# Authenticate with API
def authenticate() -> Client:
    """Authenticate with Bluesky API"""
    client = Client()
    client.login(BLUESKY_USERNAME, BLUESKY_APP_PASSWORD)
    return client
