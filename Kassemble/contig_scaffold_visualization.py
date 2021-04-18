#!/usr/bin/env python

"""

Visualization of genomic data: k-mers, contigs, assemblies. 

"""
#!/usr/bin/env python

"""

Visualization of output data from simple_spades.py. 

"""

import toytree

    
def graph_contigs(contigs.fasta)
    
  data = 

    canvas, axes, mark = toyplot.plot(
      data,
      width = 500,
      height=500,
      );
        
    
def graph_scaffolds(scaffolds.fasta)
    
  data = 

    canvas, axes, mark = toyplot.plot(
      data,
      width = 500,
      height=500,
      );
        
        

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
