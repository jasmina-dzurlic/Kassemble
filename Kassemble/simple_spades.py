#!/usr/bin/env python

"""
A simple test of calling SPades with subprocess

conda install spades -c conda-forge -c bioconda
"""

import subprocess


def call_spades(r1_file, r2_file=None, outdir="test"):
    """
    Call Spades command line tool to assemble fastq data files.
    """

    # spades must receive an input R1 file
    cmd = ["spades.py", "-1", r1_file]

    # if an R2 file is present then also append this
    if r2_file is not None:
        cmd += ["-2", r2_file]

    # add the output name
    cmd += ["-o", outdir]

    # print the command so I can see it
    print(" ".join(cmd))

    # call the command with subprocess. See the tutorial from class
    # on how to use subprocess:
    # https://nbviewer.jupyter.org/github/hackers-test/hack-7-scripting/blob/main/notebooks/nb-7.0-subprocess.ipynb
    subprocess.run(
        cmd,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )



if __name__ == "__main__":

    # test data set
    R1_FILE = "../data/ecoli_1K_1.fq.gz"
    R2_FILE = "../data/ecoli_1K_2.fq.gz"
    OUTDIR = "../ecoli-test"

    # test function, if it does not raise an error then it works
    call_spades(R1_FILE, R2_FILE, OUTDIR)

    # print contents of OUTDIR to show results
    import os
    print("results files:")
    print(os.listdir(OUTDIR))
