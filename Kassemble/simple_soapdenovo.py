#!/usr/bin/env python

"""
A simple test of calling SOAPdenovo2 with subprocess
conda install spades -c conda-forge -c bioconda
"""

import subprocess


def call_soapdenovo2 (r1_file, r2_file=None, outdir="test"):
    """
    Call SOAPdenovo command line tool to assemble fastq data files.
    """

    # spades must receive an input R1 file
    cmd = ["SOAPdenovo.py", "-1", r1_file]

    # if an R2 file is present then also append this
    if r2_file is not None:
        cmd += ["-2", r2_file]

    # add the output name
    cmd += ["-o", outdir]

    # print the command so I can see it
    print(" ".join(cmd))

    # call the command with subprocess. 

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
    OUTDIR = "/tmp/ecoli-test"

    # test function, if it does not raise an error then it works
    call_soapdenovo2 (R1_FILE, R2_FILE, OUTDIR)

    # print contents of OUTDIR to show results
    import os
    print("results files:")
    print(os.listdir(OUTDIR))
