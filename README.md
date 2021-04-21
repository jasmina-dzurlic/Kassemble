# Kassemble 
## A tool for k-mer based denovo assemblies and multispecies informed assembly graphs 

`Kassemble` is a Python package with the objective to assemble denovo contigs and scaffolds using a reference-free, k-mer based approach. `kassemble` incorporates the `SPAdes` [software tool](https://github.com/ablab/spades) and/or `SOAPdenovo2` [tool](https://github.com/aquaskyline/SOAPdenovo2) as a Python wrapper to create contigs of unique k-mers extracted from reads in a fastq file. The purpose of `kassemble` is to offer a flexible approach to entering sample names and their respective fastq data files. This makes it easy to accommodate single or paired-end data files, to combine technical replicates from different sequencing runs, or even to incorporate pooled samples. Thus, `kassemble` is intended to be easy to install, execute, and well documented. 

<p align="center">
<img src="https://github.com/jasmina-dzurlic/Kassemble/blob/main/example/assembly.png" width="500" height="400">
</p>


### In development 
The list of dependencies required by `kassemble` are: <br />
`SOAPdenovo2` <br />
`kmerkit` <br />
`subprocess` <br />
`kmerkit` <br />
`GraphBin2` <br />
`kat` <br />
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

## Working example

In this working example we will use `fasta files` of sequence data for Escherichia coli found in the data folder of this repository. 

#### Install package

```bash
conda install SPAdes SOAPdenovo2 GraphBin2 kat subprocess kmerkit -c conda-forge
``` 

#### Input data

The input for this program is a `.fasta` file containing genome seqeunces.  

<p align="center">
<img src="https://raw.githubusercontent.com/jasmina-dzurlic/Kassemble/main/example/contig.png" width="500" height="400">
</p>


#### Count k-mers

```bash
# write kmer databases for two samples to /tmp/test
kmerkit kcount --name test --workdir /tmp --sample A ecoli_1K_1.fq.gz --sample B ecoli_1K_2.fq.gz
```

#### Filter k-mers

```bash
# filter kmers to find those unique to B (not in A)
kmerkit kfilter --name test --workdir /tmp --sample A ecoli_1K_1.fq.gz --sample B ecoli_1K_2.fq.gz --mincov A 0.0 B 1.0 --maxcov A 0.0 B 1.0
```

#### Extract k-mers

```
# extract fastq reads that contain these kmers from sample B
kmerkit kextract --name test --workdir /tmp --sample A ecoli_1K_1.fq.gz --sample B ecoli_1K_2.fq.gz
```


#### Assemble k-mers 

```bash
# assemble kmers into contigs
kassemble simple_spades --name test --workdir /tmp --sample A ecoli_1K_1.fq.gz --sample B ecoli_1K_2.fq.gz
```

`kassemble` is designed for use as a CLI and stores the following output files in <output_dir> , which is set by the user:

<output_dir>/contigs.fastq contains resulting contigs <br />

<p align="center">
<img src="https://raw.githubusercontent.com/jasmina-dzurlic/Kassemble/main/example/FASTQ.png" width="400" height="200">
</p>

<p align="center">
<img src="https://raw.githubusercontent.com/jasmina-dzurlic/Kassemble/main/example/SPAdes_ecoli_graph.png" width="400" height="400">
</p>


## Create refined assembly graph (In-development)

To create a refined assembly using multi-species contig coverage, `Kassemble` uses `GraphBin2` [tool](https://github.com/Vini2/GraphBin2) in which incorporates connectivity and coverage information from assembly graphs to adjust existing binning results on contigs and to infer contigs shared by multiple species. This type of multiple species coverage is ideal for GWAS and `Kmerkit` based analysis. 

```bash
# create multi-species contig assembly graph
kassemble assembly_graph --graph ../data/assembly_graph.fastg --paths ../data/contigs.paths --outdir ../tmp --assemble spades
```

<p align="center">
<img src="https://github.com/jasmina-dzurlic/Kassemble/blob/main/example/Graphbin2.png" width="400" height="400">
</p>
Visualiation of assembly graph produced from Kassemby assembly of contigs and scaffolds. 


## Subtools for visualizing k-mer assemblies (In-development)

`Kassemble` has subtools to create visualizations of k-mers assemblies. These subtools call on the [program](https://github.com/TGAC/KAT) `KAT` to create graphs to visualize  k-mer / reads in contig assemblies such as comparisons of k-mer coverage, frequency, density, GC content, copy varitation across sequence reads, and shared exclusive content between two datasets. 


#### Spectrum of k-mers
Visualises the K-mer spectra from contig assembly. This subtool is designed to plot line graphs of one or more histograms to compare total K-mer counts between samples.

```bash
# create a histogram of k-mer spectra in a contig assembly
kassemble kmer_statistics --kat_spectra --contig_.fastq --outdir ../tmp
```

<p align="center">
<img src="(https://github.com/jasmina-dzurlic/Kassemble/blob/main/example/K-mer_spectra.PNG" width="400" height="400">
</p>


#### Comparisons of k-mers
Graph of k-mer duplication levels that correspond to copy number variation within an assembly by comparing K-mers found in sequenced reads, to K-mers found in an assembly of those reads. 

```bash
# compare copy variation in sequences
kassemble kmer_statistics --kat_comparison --contig.fastq --outdir ../tmp
```

<p align="center">
<img src="("https://github.com/jasmina-dzurlic/Kassemble/blob/main/example/K-mer%20comparison.PNG" width="400" height="400">
</p>


#### Profile k-mers
Creates a graph that illustrates coverage level of mapped k-mer reads across a sequence whith an option to isolate those of GC level content distribution. 

```bash
# create a histogram of coverage level of mapped k-mer reads across a sequence
kassemble kmer_statistics --kat_profile --contig.fastq --outdir ../tmp
```
<p align="center">
<img src="("https://github.com/jasmina-dzurlic/Kassemble/blob/main/example/K-mer_profile.PNG" width="400" height="400">
</p>


#### Density of k-mers
Creates a scatter plot, where the density is illustrated as “heat." Each point represents the number of distinct K-mers at that point. GC isolation aviable for this subtool.

```bash
# create a denisty plot of k-mers
kassemble kmer_statistics --kat_density --contig.fastq --outdir ../tmp
```

<p align="center">
<img src="("https://github.com/jasmina-dzurlic/Kassemble/blob/main/example/K-mer_density.PNG" width="400" height="400">
</p>


#### Compare datasets of k-mers

Compare shared and exclusive content between two datasets by creating a spetra mix graph to visualize k-mer spectra of columns and rows in a matrix.

```bash
# create histogram to compare k-mers
kassemble kmer_statistics --kat_dataset --contig.fastq --outdir ../tmp
```
<p align="center">
<img src="("https://github.com/jasmina-dzurlic/Kassemble/blob/main/example/K-mer_matrix.PNG" width="400" height="400">
</p>





