# bluesky_bot
Sharing thinktank stats automagically on Bluesky

# License
Code is made available under an [MIT licence](LICENSE).

# Creating your own bot
You can easily create your own bot based on this one following the steps below. This assumes that you will store your code in a GitHub repository and run the bot using GitHub Actions.

## Steps
1. **Fork this repository** 
1. **Create a Bluesky account** Set up a new Bluesky account using the handle you want your bot to have
1. **Generate an app password** [Set up an app password](https://bsky.app/settings/app-passwords) for the new account. This is what your bot will use to access the Bluesky account and is better practice than using the main password for your new account
1. **Add secrets and variables to your GitHub repo**. In your repo's _Settings_, create:
    - A GitHub Actions repository secret `BLUESKY_APP_PASSWORD`: The app password you created in Bluesky
    - A GitHub Actions repository variable `BLUESKY_USERNAME`: The username for your Bluesky account. Don't include the @ at the start of the name, but do include '.bsky.social' or the domain you use for your account

## Local env setup
1. Run `pip install -r requirements.txt`
2. Run `pre-commit install`

## Generate bump chart (from fake data currently)
1. From the project root directory
2. Run `python scripts/generate_chart.py`
3. View image in `./images`
