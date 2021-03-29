#!/usr/bin/env python
"""
Install Kassemble package. To install locally use: pip install -e .
"""

from setuptools import setup

# build command
setup(
    name="Kassemble",
    version="0.0.1",
    author="Jasmina Dzurlic",
    install_requires = ["SOAPdenovo2", "kmerkit", "subprocess"], 
    classifiers=["Programming Language :: Python :: 3"],
    #scripts= ['']
)