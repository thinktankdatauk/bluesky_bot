import os
import matplotlib.pyplot as plot
import pandas
import seaborn
import textwrap


from bump_chart.bump_chart_model import BumpChartModel
from typing import Tuple


OUTPUT_DIR = "images"
FIG_WIDTH = 6
BG_COLOR = "#060A11"
LINE_WIDTH = 3
MARKER_SIZE = 12


class BumpChartView:
    """Handles chart rendering and formatting."""

    def __init__(self, model: BumpChartModel, palette=None):
        self.model = model
        self.model.account_colors = self.model.assign_colors(palette)

    def create_figure(self) -> Tuple[plot.Figure, plot.Axes]:
        """Generates the bump chart figure and formats it."""
        figure, axes = plot.subplots(
            figsize=(FIG_WIDTH, self.model.get_total_accounts())
        )
        plot.subplots_adjust(right=0.66, left=0.07, top=0.94, bottom=0.06)
        seaborn.lineplot(
            data=self.model.data_frame,
            x="date",
            y="rank",
            hue="account",
            marker="o",
            linewidth=LINE_WIDTH,
            markersize=MARKER_SIZE,
            ax=axes,
            palette=self.model.account_colors.values(),
            markeredgewidth=0,
        )
        axes.legend().set_visible(False)
        self._format_labels(axes)
        self._apply_background_and_borders(axes)
        self._add_dotted_trailing_lines(axes)
        return figure, axes

    def save_chart(
        self, figure: plot.Figure, filename="bump_chart.png", dpi=300
    ) -> None:
        """Save the generated chart to a file."""
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        image_path = os.path.join(OUTPUT_DIR, filename)
        figure.savefig(image_path, dpi=dpi)
        print(f"Image saved at {image_path}")

    def _format_labels(self, axes: plot.Axes) -> None:
        """Format labels."""
        # x-axis
        axes.set_xlabel("")
        axes.set_xticklabels([])
        # y-axis
        axes.set_ylabel("")
        axes.invert_yaxis()
        axes.yaxis.tick_right()
        axes.yaxis.set_label_position("right")
        # latest_ranks
        latest_ranks = self.model.get_latest_rankings()
        axes.set_yticks(latest_ranks.index)
        axes.set_yticklabels([latest_ranks[rank] for rank in latest_ranks.index])
        # latest_follower_counts
        latest_follower_counts = self.model.get_latest_follower_counts()
        # set colours
        for label in axes.get_yticklabels():
            label.set_color(self.model.account_colors.get(label.get_text(), "white"))
        # format labels
        axes.set_yticklabels(
            [
                "\n".join(
                    textwrap.wrap(label.get_text(), 20)
                    + ["- followers: " + str(latest_follower_counts[label.get_text()])]
                )
                for label in axes.get_yticklabels()
            ]
        )

    def _apply_background_and_borders(self, axes: plot.Axes) -> None:
        """Apply a dark background and remove borders."""
        axes.set_facecolor(BG_COLOR)
        plot.gcf().set_facecolor(BG_COLOR)
        borders = axes.spines.values()
        for border in borders:
            border.set_visible(False)

    def _add_dotted_trailing_lines(self, axes: plot.Axes) -> None:
        """Add dotted lines extending from the first data point."""
        for account in self.model.data_frame["account"].unique():
            account_data = self.model.data_frame[
                self.model.data_frame["account"] == account
            ]
            first_entry = account_data.iloc[0]
            start_date = first_entry["date"] - pandas.Timedelta(days=5)
            first_rank = first_entry["rank"]
            color = self.model.account_colors[account]
            axes.plot(
                [start_date, first_entry["date"]],
                [first_rank, first_rank],
                linestyle="dotted",
                linewidth=LINE_WIDTH,
                color=color,
            )
