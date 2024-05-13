import os
from typing import List
from matplotlib import pyplot as plot

RESOURCES = os.environ.get('RESOURCES')


def create_bar_plot(labels: List[str],
                    values: List[any],
                    colors: List[str],
                    label_names: List[str],
                    title: str,
                    filename: str) -> None:
    plot.bar(labels, values, color=colors)
    plot.xlabel(label_names[0])
    plot.ylabel(label_names[1])
    plot.title(title)
    plot.savefig(RESOURCES + filename)
