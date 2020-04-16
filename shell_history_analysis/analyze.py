"""Functions to analyze a shell history."""


# Core Library modules
import os

# Third party modules
import matplotlib.pyplot as plt
import pandas as pd
import yaml
from pkg_resources import resource_filename

# First party modules
from shell_history_analysis.shell_io import read_history


def main(
    history_filepath: str,
    shell: str,
    grouping_filepath: str = None,
    apply_grouping: bool = True,
) -> pd.DataFrame:
    print(f"Assumed shell: {shell}")
    df = read_history(history_filepath, shell)

    if apply_grouping:
        if grouping_filepath is None:
            grouping_filepath = resource_filename(__name__, "grouping.yaml")
        grouping_filepath = os.path.abspath(grouping_filepath)
        with open(grouping_filepath) as f:
            grouping = yaml.safe_load(f)
        grouping_t = {}
        for to, from_list in grouping.items():
            for from_str in from_list:
                grouping_t[from_str] = to
        df["base_command"] = df["base_command"].map(
            lambda n: grouping_t.get(n, n)
        )
    print(f"Grouping filepath: {grouping_filepath}")

    counts = df.base_command.value_counts()
    min_occurences = 20
    if max(counts) < min_occurences:
        min_occurences = max(max(counts) - 10, min(counts))
    counts = counts[counts >= min_occurences]
    print()
    print("Group                   Counts")
    print("------------------------------")
    print(counts)
    min_date = min(df["date"])
    max_date = max(df["date"])
    plt.title(
        f"Command distribution from {min_date:%Y-%m-%d} "
        f"to {max_date:%Y-%m-%d}\nmin occurences = {min_occurences}"
    )
    ax = counts.plot(kind="pie", figsize=(8, 8), title="")
    ax.set_ylabel("")
    target = os.path.abspath("history.png")
    print(f"Writing image to {target}")
    plt.savefig(target)
    return df
