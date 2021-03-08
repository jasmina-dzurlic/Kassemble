# Kassemble 
  
### Utility of proposal
`kassemble` is a Python package with the objective to assemble denovo contigs using a reference-free, k-mer based approach. The purpose of `kassemble` is to offer a flexible approach to entering sample names and their respective fastq data files. This makes it easy to accommodate single or paired-end data files, to combine technical replicates from different sequencing runs, or even to incorporate pooled samples. Thus, `kassemble` is intended to be easy to install, execute, and well documented. `kassemble` incorporates the `SPAdes` [software tool](https://github.com/ablab/spades) as a Python wrapper to create contigs of unique k-mers extracted from reads in a fastq file.  
<img src="contig.png" width="500">

### Data sources and input
Genomic data contained in a .fastq format is the input data for `kassemble`. 

<img src="FASTQ.png" width="500">


### User interaction and output
The preanalysis of the data that is imported into `kassemble` is produced by `kmerkit`. As a wrapper around `SPades`, `kassembly` is intended to make it easier and added as an addition to the `kmerkit` [tool kit](https://github.com/eaton-lab/kmerkit.git) pipeline. `kmerkit` counts kmers using `kcount`, filters unique kmers using `kfilter`, then extracts unqiue k-mers using `kextract`.

```bash
# write kmer databases for two samples to /tmp/test
kmerkit kcount --name test --workdir /tmp --sample A A.fastq.gz --sample B B.fastq.gz

# filter kmers to find those unique to B (not in A)
kmerkit kfilter --name test --workdir /tmp --mincov A 0.0 B 1.0 --maxcov A 0.0 B 1.0

# extract fastq reads that contain these kmers from sample B
kmerkit kextract --name test --workdir /tmp --samples A A.fastq.gz 
```

Then `kassemble` incorporates the data produced from the previous pipeline to assemble k-mers into denovo conitgs. 

```bash
# assemble kmers into contigs
kassemble --name assembled --workdir /tmp-assembled/ --sample B B.fastq.gz 
```

`kassemble` is designed for use as a CLI and stores the following output files in <output_dir> , which is set by the user:

<output_dir>/contigs.fastq contains resulting contigs <br />
<output_dir>/assembly_graph.gfa contains assembly graph of contigs

For example, below is an example of `contigs.fastq` as a `assembly_graph.gfa` for E. coli produced by SPAdes.  


<img src="SPAdes_ecoli_graph.png" width="400">
Figure 1. E. coli contig assembly graph created using SPAdes. 


### Installation 
```bash
# conda install kassembly -c conda-forge -c bioconda

git clone https://github.com/jasmina-dzurlic/Kassemble.git
cd kassemble
pip install -e .
``` 

### Related tools
`SOAPdenovo2` is a [contig assembly tool](https://github.com/aquaskyline/SOAPdenovo2) that performs similar assemblies of contigs. The shortcomings of `SOAPdenovo2` is that it is designed for short read assemblies and small genomes compared to `SPAdes` in which utilizes long-reads in a short-read assembly. In additon, `SPAdes`incorporates long reads to scaffold contigs from a short-read assembly. Beacuse of this, I believe `SPAdes` is better to incoporate into `kassemble` rather than `SOAPdenovo2`. `kassemble` is different from `SPAdes`and `SOAPdenovo2` in terms of user friendliness and that it is intended to be an addition to a more robust pipeline, `kmerkit`, in which performs evolutionary analyses using kmer counts, frequencies, and comparisons with or without the context of a reference genome.
