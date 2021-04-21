
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

    
 def call_kat_spectra ( graph="assembly_graph.fastg", outdir="test", assembler="spades", paths="contigs.paths"):

    """
    Call kat command line tool to assemble fastq data files.
    """

    # spa must receive an assembly graph file
    cmd1 = ["kat.py", "-graph", assembly_graph.fastg]

    # add the output name
    cmd1 += ["-output", outdir]
    
    # add the output name
    cmd1 += ["-assembler", spades]
    
    # add the output name
    cmd1 += ["-paths", contigs.paths outdir]

    # print the command so I can see it
    print(" ".join(cmd1))

    # call the command with subprocess. 
    subprocess.run(
        cmd1,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )

 def call_kat_spectra ( graph="assembly_graph.fastg", outdir="test", assembler="spades", paths="contigs.paths"):

    """
    Call kat command line tool to assemble fastq data files.
    """

    # spa must receive an assembly graph file
    cmd2 = ["kat.py", "-graph", assembly_graph.fastg]

    # add the output name
    cmd2 += ["-output", outdir]
    
    # add the output name
    cmd2 += ["-assembler", spades]
    
    # add the output name
    cmd2 += ["-paths", contigs.paths outdir]

    # print the command so I can see it
    print(" ".join(cmd2))

    # call the command with subprocess. 
    subprocess.run(
        cmd2,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )


 def call_kat_density ( graph="assembly_graph.fastg", outdir="test", assembler="spades", paths="contigs.paths"):

    """
    Call kat command line tool to assemble fastq data files.
    """

    # spa must receive an assembly graph file
    cmd3 = ["kat.py", "-graph", assembly_graph.fastg]

    # add the output name
    cmd3 += ["-output", outdir]
    
    # add the output name
    cmd3 += ["-assembler", spades]
    
    # add the output name
    cmd3 += ["-paths", contigs.paths outdir]

    # print the command so I can see it
    print(" ".join(cmd3))

    # call the command with subprocess. 
    subprocess.run(
        cmd3,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )

 def call_kat_profile ( graph="assembly_graph.fastg", outdir="test", assembler="spades", paths="contigs.paths"):

    """
    Call kat command line tool to assemble fastq data files.
    """

    # spa must receive an assembly graph file
    cmd4 = ["kat.py", "-graph", assembly_graph.fastg]

    # add the output name
    cmd4 += ["-output", outdir]
    
    # add the output name
    cmd4 += ["-assembler", spades]
    
    # add the output name
    cmd4 += ["-paths", contigs.paths outdir]

    # print the command so I can see it
    print(" ".join(cmd4))

    # call the command with subprocess. 
    subprocess.run(
        cmd4,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )
 
    
  def call_kat_comparison ( graph="assembly_graph.fastg", outdir="test", assembler="spades", paths="contigs.paths"):

    """
    Call kat command line tool to assemble fastq data files.
    """

    # spa must receive an assembly graph file
    cmd5 = ["kat.py", "-graph", assembly_graph.fastg]

    # add the output name
    cmd5 += ["-output", outdir]
    
    # add the output name
    cmd5 += ["-assembler", spades]
    
    # add the output name
    cmd5 += ["-paths", contigs.paths outdir]

    # print the command so I can see it
    print(" ".join(cmd5))

  # call the command with subprocess. 
    subprocess.run(
        cmd5,         # this is the command
        check=True,  # this checks whether it finished successfully
        stderr=subprocess.STDOUT,  # these last two args make it run quietly
        stdout=subprocess.DEVNULL, # without printing tons of into to stdout
    )
 

  def call_kat_matrix ( graph="assembly_graph.fastg", outdir="test", assembler="spades", paths="contigs.paths"):

    """
    Call kat command line tool to assemble fastq data files.
    """

    # spa must receive an assembly graph file
    cmd6 = ["kat.py", "-graph", assembly_graph.fastg]

    # add the output name
    cmd6 += ["-output", outdir]
    
    # add the output name
    cmd6 += ["-assembler", spades]
    
    # add the output name
    cmd6 += ["-paths", contigs.paths outdir]

    # print the command so I can see it
    print(" ".join(cmd5))

  # call the command with subprocess. 
    subprocess.run(
        cmd6,         # this is the command
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
    call_kat(GRAPH, ASSEMBLER, PATHS, OUTDIR)

    # print contents of OUTDIR to show results
    import os
    print("results files:")
    print(os.listdir(OUTDIR))
