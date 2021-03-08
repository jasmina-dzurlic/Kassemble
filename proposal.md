# Kassemble 

`kassemble` is a Python package with the objective to assemble fastq reads into denovo contigs to map the location of genes in a genome. 

### Utility of proposal
`kassemble` will assemble reference-free genome wide associations (GWAS) using a k-mer based approach. 



<img src="contig.png" width="700">

### Data sources and input
Genomic data in a .fastq format is the input data for `kassemble`. 

<img src="FASTQ.png" width="600">

The preanalysis of the data that is used to import into `kassemble` will be produced by `kmerkit`. `kmerkit` counts kmers using `kcount`, filters unique kmers using `kfilter`, then extracts unqiue k-mers using `kextract`.

```bash
# write kmer databases for two samples to /tmp/test
kmerkit kcount --name test --workdir /tmp --sample A A.fastq.gz --sample B B.fastq.gz

# filter kmers to find those unique to B (not in A)
kmerkit kfilter --name test --workdir /tmp --mincov A 0.0 B 1.0 --maxcov A 0.0 B 1.0

# extract fastq reads that contain these kmers from sample B
kmerkit kextract --name test --workdir /tmp --samples A A.fastq.gz 
```

Then `kassembly` will be added to the previous pipeline to assebmle the unique k-mers into denovo conitgs. 

```bash
# assemble kmers into contigs
kassemble --name assembled --workdir /tmp-assembled/ --sample B B.fastq.gz 
```

### User interaction and output 

Kassemble stores the following output files in <output_dir> , which is set by the user:

<output_dir>/contigs.fasta contains resulting contigs <br />
<output_dir>/assembly_graph.gfa contains assembly graph of contigs

[add description sentence]


<img src="SPAdes_ecoli_graph.png" width="400">
Figure 1. E. coli contig assembly graph created using SPAdes. 


### Installation 
```bash
# conda install kassembly -c conda-forge -c bioconda

git clone https://github.com/jasmina-dzurlic/Kassemble.git
cd kassembly
pip install -e .
``` 

### Related tools
`SPAdes` is a related tool that will be incorporated as in `Kassembly` with a python wrapper to perform de novo contig assemblies. The [documentation](https://github.com/ablab/spades) for `SPAdes` provides more detailed information about the program. `SOAPdenovo2` is also a contig assembly tool that performs similar assemblies and more information about this program can be found [here](https://github.com/aquaskyline/SOAPdenovo2). The shortcomings of `SOAPdenovo2` is that it is designed for short read assemblies and small genomes compared to `SPAdes` in which utilizes long-reads in a short-read assembly. In additon, `SPAdes`incorporates long reads to scaffold contigs from a short-read assembly. 
