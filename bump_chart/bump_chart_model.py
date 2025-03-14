import pandas
import seaborn


from typing import Dict


class BumpChartModel:
    """Processes data for a bump chart, including ranking and color mapping."""

    def __init__(self, data: dict, palette=None):
        self.raw_data = data
        self.data_frame = self._convert_to_dataframe()
        self.account_colors = self.assign_colors(palette)

    def _convert_to_dataframe(self) -> pandas.DataFrame:
        """Convert raw data into a structured long-format DataFrame with rankings."""
        data_frame = pandas.DataFrame(self.raw_data)
        data_frame = data_frame.melt(
            id_vars=["date"],
            var_name="account",
            value_name="followers",
        )

        data_frame["date"] = pandas.to_datetime(data_frame["date"])
        data_frame["rank"] = (
            data_frame.groupby("date")["followers"]
            .rank(ascending=False, method="first")
            .astype(int)
        )
        return data_frame

    def assign_colors(self, palette) -> Dict[str, any]:
        """Generate unique colors for each account using the specified palette."""

        if palette is None:
            palette = seaborn.color_palette("colorblind")

        accounts = self.data_frame["account"].unique()
        return {
            account: palette[i % len(palette)] for i, account in enumerate(accounts)
        }

    def get_latest_rankings(self) -> pandas.Series:
        """Retrieve rankings for the most recent date."""
        latest_date = self.data_frame["date"].max()
        latest_data = self.data_frame[self.data_frame["date"] == latest_date]
        return latest_data.set_index("rank")["account"].sort_index()

    def get_latest_follower_counts(self) -> pandas.Series:
        """Retrieve rankings for the most recent date."""
        latest_date = self.data_frame["date"].max()
        latest_data = self.data_frame[self.data_frame["date"] == latest_date]
        return latest_data.set_index("account")["followers"]

    def get_total_accounts(self) -> int:
        """Return the number of unique accounts in the dataset."""
        return self.data_frame["account"].nunique()
