#!/usr/bin/env python

"""
Creating an assembly graph with GraphBin2
(https://github.com/Vini2/GraphBin2)

Install Graph Bin 2:
conda env create -f environment.yml
conda activate graphbin

optional arguments:
  --graph GRAPH         path to the assembly graph file
  --output OUTPUT       path to the output folder
  --assembler ASSEMBLER
                        name of the assembler used (SPAdes, SGA or MEGAHIT). 
  --paths PATHS         path to the contigs.paths file, only needed for SPAdes
  --contigs CONTIGS     path to the final.contigs.fa file, only needed for MEGAHIT
"""

import subprocess


def call_graphbin2( graph="assembly_graph.fastg", outdir="test", assembler="spades", paths="contigs.paths"):

    """
    Call Graphbin2 command line tool to assemble fastq data files.
    """

    # spa must receive an assembly graph file
    cmd = ["graphbin2.py", "-graph", assembly_graph.fastg]

    # add the output name
    cmd += ["-output", outdir]
    
    # add the output name
    cmd += ["-assembler", spades]
    
    # add the output name
    cmd += ["-paths", contigs.paths outdir]

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
    GRAPH = "../data/assembly_graph.fastg"
    OUTDIR = "../tmp"
    ASSEMBLER = "spades"
    PATHS = "../data/contigs.paths"
       

    # test function, if it does not raise an error then it works
    call_graphbin2(GRAPH, ASSEMBLER, PATHS, OUTDIR)

    # print contents of OUTDIR to show results
    import os
    print("results files:")
    print(os.listdir(OUTDIR))
