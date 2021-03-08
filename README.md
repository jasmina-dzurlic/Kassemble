# Kassemble 
`kassemble` is a Python package with the objective to assemble denovo contigs using a reference-free, k-mer based approach. The purpose of `kassemble` is to offer a flexible approach to entering sample names and their respective fastq data files. This makes it easy to accommodate single or paired-end data files, to combine technical replicates from different sequencing runs, or even to incorporate pooled samples. Thus, `kassemble` is intended to be easy to install, execute, and well documented. `kassemble` uses the `SPAdes` [software tool](https://github.com/ablab/spades) to create contigs of unique k-mers extracted from reads in a fastq file. As a wrapper around `SPades`, `kassembly` is intended to make it easier and added as an addition to the `kmerkit` [tool kit](https://github.com/eaton-lab/kmerkit.git) pipeline. 

<img src="contig.png" width="500">

### In development 
