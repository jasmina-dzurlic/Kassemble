# Kassemble 
## Denovo contig assembly tool for genetic sequences

`kassemble` is a Python package with the objective to assemble denovo contigs using a reference-free, k-mer based approach. `kassemble` incorporates the `SPAdes` [software tool](https://github.com/ablab/spades) and/or `SOAPdenovo2` [tool](https://github.com/aquaskyline/SOAPdenovo2) as a Python wrapper to create contigs of unique k-mers extracted from reads in a fastq file. The purpose of `kassemble` is to offer a flexible approach to entering sample names and their respective fastq data files. This makes it easy to accommodate single or paired-end data files, to combine technical replicates from different sequencing runs, or even to incorporate pooled samples. Thus, `kassemble` is intended to be easy to install, execute, and well documented. ![alt tag](https://raw.githubusercontent.com/jasmina-dzurlic/Kassemble/main/example/Contig%20schematic.png)
### In development 
The list of dependencies required by `kassemble` are: <br />
`SOAPdenovo2` <br />
`kmerkit` <br />
`subprocess` <br />
`kmerkit` <br />
`spades` vr 3.12.0  <br />

The following command in `conda` installs these packages if they are not previously installed: <br /> 
```bash
conda install SPAdes SOAPdenovo2 subprocess kmerkit -c conda-forge
``` 

As `kassemble` undergoes development, it can currently be installed locally using the following command to clone this repository to your local machine:

```bash
git clone https://github.com/jasmina-dzurlic/Kassemble.git
cd kassemble
pip install -e .
``` 

### Working example

In this working example we will use `fasta files` of sequence data for Escherichia coli found in the data folder of this repository. 

##### Install package

```bash
conda install SPAdes SOAPdenovo2 subprocess kmerkit -c conda-forge
``` 

##### Input data

The input for this program is a `.fasta` file containing genome seqeunces.  

![alt tag](https://raw.githubusercontent.com/jasmina-dzurlic/Kassemble/main/example/contig.png)

##### Count k-mers

```bash
# write kmer databases for two samples to /tmp/test
kmerkit kcount --name test --workdir /tmp --sample A ecoli_1K_1.fq.gz --sample B ecoli_1K_2.fq.gz
```

##### Filter k-mers

```bash
# filter kmers to find those unique to B (not in A)
kmerkit kfilter --name test --workdir /tmp --mincov A 0.0 B 1.0 --maxcov A 0.0 B 1.0
```

##### Extract k-mers

```
# extract fastq reads that contain these kmers from sample B
kmerkit kextract --name test --workdir /tmp --samples A ecoli_1K_1.fq.gz 
```


##### Assemble k-mers 

```bash
# assemble kmers into contigs
kassemble --name assembled --workdir /tmp-assembled/ --sample ecoli_1K_1.fq.gz 
```

`kassemble` is designed for use as a CLI and stores the following output files in <output_dir> , which is set by the user:

<output_dir>/contigs.fastq contains resulting contigs <br />

![alt tag](https://raw.githubusercontent.com/jasmina-dzurlic/Kassemble/main/example/FASTQ.png)

<output_dir>/assembly_graph.gfa contains assembly graph of contigs

![alt tag](https://raw.githubusercontent.com/jasmina-dzurlic/Kassemble/main/example/SPAdes_ecoli_graph.png)

