"""Test the shell_io module."""

# First party modules
from shell_history_analysis.shell_io import extract_command_list


def test_extract_command_list_zsh():
    """Test the extract_command_list command with a zsh like input."""
    content = """ 9597  5.1.2020 11:23  git status
 9598  5.1.2020 11:23  cd .idea
 9599  5.1.2020 11:23  ls
 9600  5.1.2020 11:23  ..
 9601  5.1.2020 11:23  rm -rf .idea
 9602  5.1.2020 11:24  rm n26-csv-transactions.csv
 9603  5.1.2020 11:24  ..
 9604  5.1.2020 11:24  git status .
 9605  5.1.2020 11:24  cd gunicorn/worker-performance
 9606  5.1.2020 11:24  ls
 9607  5.1.2020 11:24  git add app.py
 9608  5.1.2020 11:24  isort app.py"""
    df = extract_command_list(content, shell="zsh")
    assert len(df) == 12
