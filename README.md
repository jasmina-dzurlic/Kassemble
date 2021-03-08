# Kassemble 
`kassemble` is a Python package with the objective to assemble denovo contigs using a reference-free, k-mer based approach. `kassemble` incorporates the `SPAdes` [software tool](https://github.com/ablab/spades) as a Python wrapper to create contigs of unique k-mers extracted from reads in a fastq file. The purpose of `kassemble` is to offer a flexible approach to entering sample names and their respective fastq data files. This makes it easy to accommodate single or paired-end data files, to combine technical replicates from different sequencing runs, or even to incorporate pooled samples. Thus, `kassemble` is intended to be easy to install, execute, and well documented. 

<img src="contig.png" width="500">

### In development 
 
```bash
# conda install kassembly -c conda-forge -c bioconda

git clone https://github.com/jasmina-dzurlic/Kassemble.git
cd kassemble
pip install -e .
``` 
