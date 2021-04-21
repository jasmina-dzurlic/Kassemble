
#!/usr/bin/env python

"""
Producing assembly statisitcs with The K-mer Analysis Toolkit (KAT)
(https://github.com/TGAC/KAT)

Install:
bioconda install kat

optional arguments:
 
--spectra-hist
--gcp
--comp
--sect
--filter
--denisty

"""

import subprocess

    
 def call_kat_spectra ( hist_file="contig.fastq", outdir="test")

    """
    Call kat command line tool to create spectra histogram.
    """

    # receive an acontig file with k-mers file
    cmd1 = ["kat.py", "hist_file", contig.fastq]

    # add the output name
    cmd1 += ["-output", outdir]
    
    # add the output name

    # print the command so I can see it
    print(" ".join(cmd1))

    # call the command with subprocess. 
    subprocess.run(
        cmd1,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )

 def call_kat_denisty ( matrix_file="matrix.", outdir="test":

    """
    Call kat command line tool to creat denisty graph of k-mers.
    """

    # recieve matrix fie
    cmd2 = ["kat.py", "-matrix_file", martix.]

    # add the output name
    cmd2 += ["-output", outdir]
    
    # print the command so I can see it
    print(" ".join(cmd2))

    # call the command with subprocess. 
    subprocess.run(
        cmd2,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )


 def call_kat_profile ( profile="contigs.fastq", outdir="test"):

    """
    Call kat command line tool to graph of GC content in k-mers/reads
    """

    # spa must receive an assembly graph file
    cmd3 = ["kat.py", "-profile", contigs.fastq]

    # add the output name
    cmd3 += ["-output", outdir]

    # print the command so I can see it
    print(" ".join(cmd3))

    # call the command with subprocess. 
    subprocess.run(
        cmd3,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )

                       
 def call_kat_comparison ( contigs_file="contigs.fastg", outdir="test""):

    """
    Call kat command line tool to graph of the copy number spectra of WGS data compared against an assembly
    """

    # spa must receive an assembly graph file
    cmd4 = ["kat.py", "-contigs", contigs.fastg]

    # add the output name
    cmd4 += ["-output", outdir]

    # print the command so I can see it
    print(" ".join(cmd4))

    # call the command with subprocess. 
    subprocess.run(
        cmd4,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )
 
    
  def call_kat_dataset (contigs="contigs.fastg", outdir="test"):

    """
    Call kat command line tool to create graph of datasets
    """

    # spa must receive an assembly graph file
    cmd5 = ["kat.py", "-contigs", contigs.fastg]

    # add the output name
    cmd5 += ["-output", outdir]

    # print the command so I can see it
    print(" ".join(cmd5))

  # call the command with subprocess. 
    subprocess.run(
        cmd5,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )
 
                          
    

    if __name__ == "__main__":

    # test data set
    CONTIGS = "../data/assembly_graph.fastg"
    OUTDIR = "../tmp"
    MATRIX = "spades"
   

    # test function, if it does not raise an error then it works
    call_kat(CONTIGS, OUTDIR, MATRIX)

    # print contents of OUTDIR to show results
    import os
    print("results files:")
    print(os.listdir(OUTDIR))
