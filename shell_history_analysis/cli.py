#!/usr/bin/env python

"""Analyze a shell history."""

# Third party modules
import click

# First party modules
from shell_history_analysis.analyze import main


@click.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option("--shell", type=click.Choice({"zsh", "fish", "bash"}))
@click.option(
    "--grouping",
    type=click.Path(exists=True),
    help="Path to a YAML file which groups commands together",
)
def entry_point(filename: str, shell: str, grouping: str):
    main(filename, shell, grouping)
