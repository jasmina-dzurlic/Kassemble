#!/usr/bin/env python
"""
Assembles unique kmers in fastq data files using SPAdes to create
denovo contigs. 

Kcount -> Kfilter -> Kextract -> KASSEMBLE

Links:
https://github.com/ablab/spades

"""

import os
import sys
import subprocess
import spades
import pandas as pd
from loguru import logger
from kmerkit import Kcount
from kmerkit import Kfilter
from kmerkit import Kextract


class Kassemble:
    """
    Assemble fastq reads containing target kmers. 

    Files 

    Parameters
    ==========
    name (str):
        Prefix name for the fastq files that will be written. 
        Example: <workdir>/k_assemble_<name>_<sample_name>.fastq
    workdir (str):
        Working directory where new filtered fastq files will be written.
        Examples: '/tmp' or '/tmp/newfastqs'.
    kmerfile (str):
        File with fastq of reads with unique kmers. 
    kmersize (str):
        Size of kmers
        SPAdes default: -k 21,33,55,77,99,127
    outputdir (str):
        Directory where outputs are stored. 
        
    """
    
    def __init__(
        self, 
        name, 
        workdir, 
        kmerfile,
        kmersize,
        outputdir
        ):

    #store input parameters
        self.name = name
        self.workdir = os.path.realpath(os.path.expanduser(workdir))
        self.kmerfile = kmerfile
        self.kmersize = kmersize
        self.outputdir = output directory
       
    # output file prefix
        self.prefix = os.path.join(self.workdir, f"kassemble_{self.name}")


    def assemble_contig(self):
        """
        Assemble contigs using SPAdes by executing subproccess. 
        TODO: check input data options for SPAdes and how to set -1 to be more than one option.
        
        """
     
        # create command: 'spades -k 21,33,55,77,99,127 <your reads> -o spades_output'
        cmd = [
            "spades", #changed this line
            "-o{}".format(self.output),
            "-1{}".format(self.kmerfile),
            "-k{}".format(self.kmersize),
            self.workdir, #what does this do? Since it's not in the command above you're trying to create
        ]

        # call subprocess on the command
        logger.debug(" ".join(cmd))
        out = subprocess.run(
            cmd,
            stderr=subprocess.STDOUT, 
            stdout=subprocess.PIPE,
            check=True,
            cwd=self.workdir,
        )

    def some_graph_tool(self):
        """
        Creates assembly graph
        """
        pass


if __name__ == "__main__":

    # test dataset
    FILES = "~/Documents/kmerkit/data/amaranths/hybridus_*.fastq.gz"
    FASTQ_DICT = get_fastq_dict_from_path(FILES, "_R")

    import kassemble
    
    # example
    
    Assemble = Kassemble(
        name="hybridus", 
        workdir="/tmp/", 
        fastq_dict=FASTQ_DICT,
        kmerfile="~/Documents/kmerkit/data/amaranths/hybridus_*.fastq.gz"

    )
    # print(assemble.statsdf.T)
    counter.run()

    # statdf is saved to the workdir as a fastq
    # print(asseble.statsdf.T)

