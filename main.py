import random


from bump_chart_model import BumpChartModel
from bump_chart_view import BumpChartView


if __name__ == "__main__":
    sample_data = {
        "date": ["2025-02-21", "2025-02-28", "2025-03-07"],
        "Institute of Development Studies": [6005, 8000, 8500],
        "The Work Foundation": [4000, 6600, 8200],
        "Chatham House": [6450, 8002, 9000],
        "Institute for Government": [6000, 8200, 10000],
        "The Institute for Employment Rights": [5000, 5000, 6000],
        "Royal United Services Institute": [6000, 6000, 8000],
        "Centre for Economic and Policy Research": [5100, 5800, 5900],
        "Equality and Human Rights Commission": [2200, 3040, 3000],
        "Centre for European Policy Studies": [2000, 2300, 4000],
        "Centre for European Reform": [4100, 4300, 5500],
    }

    model = BumpChartModel(sample_data)
    # palette generated using: https://mokole.com/palette.html
    test_pallet_bright = [
        "#117411",
        "#2244ff",
        "#b03060",
        "#ff0000",
        "#ffff00",
        "#00ff00",
        "#00dddd",
        "#ff00dd",
        "#6495ed",
        "#dddead",
    ]

    test_pallet_muted = [
        "#167288",  # blues
        "#8cdaec",  # blues
        "#b45248",  # reds
        "#d48c84",  # reds
        "#a89a49",  # yellows
        "#d6cfa2",  # yellows
        "#3cb464",  # greens
        "#9bddb1",  # greens
        "#643c6a",  # purples
        "#836394",  # purples
    ]
    random.shuffle(test_pallet_muted)

    view = BumpChartView(model, palette=test_pallet_muted)
    figure, axes = view.create_figure()
    view.save_chart(figure)
