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
1. **Configure GitHub Actions** Modify [call_api.yaml](.github\workflows\call_api.yaml) - a YAML file that controls how the bot should run on GitHub Actions. By changing the `cron` line you can change the frequency with which the bot calls pulls in data using the Bluesky API (a handy tool for working out how to set `cron` schedules is [Crontab Guru](https://crontab.guru/)).

## Local env setup
1. Run `pip install -r requirements.txt`
1. Run `pre-commit install`
1. Copy [`.env.example`](.env.example) and rename the copy `.env`. Replace '`xxxxxxxxxxx`' in the file with [the app password you created in Bluesky and the username for your Bluesky account](#steps).

## Generate bump chart (from fake data currently)
1. From the project root directory
2. Run `python generate_chart.py`
3. View image in `./images`

## Pull in Bluesky follower counts
1. From the project root directory, run `python call_api.py`
1. View data in `./data/thinktanks_bluesky_data.csv`
