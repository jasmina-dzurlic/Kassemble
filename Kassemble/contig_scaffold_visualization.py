
#!/usr/bin/env python

"""
Visualization of contigs and scaffolds output data from simple_spades.py. 
"""

import toyplot

 """
 Graphs contigs assembled by simple_spades.py
 """
    
def graph_contigs(contigs.fasta)
 
 """
 Graphs contigs assembled by simple_spades.py
 """
    
  data = (contigs.fasta)

    canvas, axes, mark = toyplot.plot(
      data,
      width = 500,
      height=500,
      color='orange',
 );
       
        
def graph_contigs(scaffolds.fasta)

 """
 Graphs scaffolds assembled by simple_spades.py
 """
    
  data = (scaffolds.fasta)

    canvas, axes, mark = toyplot.plot(
      data,
      width = 500,
      height=500,
      color='orange',
 );    

 
if __name__ == "__main__":

    # test function, if it does not raise an error then it works
    graph_contigs (contigs.fasta)
    graph_scaffolds(scaffolds.fasta)

    # print contents of OUTDIR to show results
    print("contigs.graph" "scaffolds.graph")

