#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""shell history analysis."""

# Third party
from setuptools import setup

setup(
    package_data={"shell_history_analysis": ["grouping.yaml"]},
    install_requires=[
        "click",
        "python-dateutil",
        "matplotlib",
        "pandas",
        "pyaml",
    ],
    tests_require=[
        "pytest",
        "pytest-cov",
        "pytest-mccabe",
        "pytest-flake8",
        "simplejson",
    ],
)
