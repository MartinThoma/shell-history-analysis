"""Parsing the shell history."""

# Core Library modules
import re

# Third party modules
import dateutil.parser
import pandas as pd


def read_history(filename: str, shell: str) -> pd.DataFrame:
    with open(filename) as f:
        content = f.read()
    df = extract_command_list(content, shell=shell)
    df["cleaned_command"] = df["command"]
    df = prefix_removal(df, prefix="sudo")
    df = prefix_removal(df, prefix="time")
    new = df["cleaned_command"].str.split(" ", expand=True)
    df["base_command"] = new[0]
    return df


def extract_command_list(content: str, shell: str) -> pd.DataFrame:
    commands = []
    lines = content.rstrip().split("\n")
    # This is the ZSH history result pattern:
    #                9      13.5.2018 10:11  cd fonts
    # You might need to adjust the pattern!
    if shell == "zsh":
        pattern = (
            r"\s+(?P<number>\d+)"
            r"\s+(?P<date>\d+\.\d+\.\d+ \d+:\d+)"
            r"\s+(?P<command>.+)"
        )
    elif shell == "bash":
        pattern = r"\s+(?P<number>\d+)\s+(?P<command>.+)"
    else:
        pattern = r"(?P<command>.+)"

    for line in lines:
        re_result = re.search(pattern, line, re.IGNORECASE)
        if re_result is None:
            continue
        groups = re_result.groupdict()
        commands.append(
            (
                groups.get("number", None),
                dateutil.parser.parse(groups.get("date", "1970-01-01")),
                groups.get("command", None),
            )
        )
    df = pd.DataFrame(commands, columns=["number", "date", "command"])
    return df


def clean_prefix(x: str, prefix: str) -> str:
    """Remove a prefix and all options from the command x."""
    if not x.startswith(prefix):
        return x
    x = x[len(prefix) :]
    i = 0
    last_was_minus = False
    for i, char in enumerate(x):  # noqa: B007
        if last_was_minus and char == " ":
            last_was_minus = False
        if char == "-":
            last_was_minus = True
        if char not in ["-", " "] and not last_was_minus:
            break
    x = x[i:]
    return x


def prefix_removal(df: pd.DataFrame, prefix: str) -> pd.DataFrame:
    """
    Annotate commands having `prefix` and remove `prefix` from cleaned_command.

    Parameters
    ----------
    df : pd.DataFrame
    prefix : str

    Returns
    -------
    df : pd.DataFrame
    """
    df[prefix] = df["cleaned_command"].str.startswith(f"{prefix} ")
    df["cleaned_command"] = df["cleaned_command"].map(
        lambda x: clean_prefix(x, prefix=prefix)
    )
    return df
