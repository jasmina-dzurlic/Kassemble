#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# Build setup.
setup(
    name="Kassemble",
    version="0.0.1",
    url="https://github.com/jasmina-dzurlic/Kassemble.git",
    author="Jasmina Dzurlic",
    author_email="jd3451@columbia.edu",
    description="A package to asseble denovo contigs with a reference-free, k-mer based approach.",
)
