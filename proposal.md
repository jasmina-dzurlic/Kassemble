# Kassemble 

`kassemble` assembles extracted k-mers into denovo contigs to map the location in a genome.\ 

### Utility of proposal
My program will assemble reference-free genome wide associations (GWAS) with a k-mer based approach. For the class project, I will build the `kassemble` module that will assemble unique k-mers into denovo contigs in order to map the location of genetic variants detected. 

### Data sources and input
`kassemble` will use genomic data in a .fastq format and phenotype data in a .csv format. 


### User interaction and output 
My program...

```bash
# write kmer databases for two samples to /tmp/test
kmerkit kcount --name test --workdir /tmp --sample A A.fastq.gz --sample B B.fastq.gz

# filter kmers to find those unique to B (not in A)
kmerkit kfilter --name test --workdir /tmp --mincov A 0.0 B 1.0 --maxcov A 0.0 B 1.0

# extract fastq reads that contain these kmers from sample B
# *** this produces the filtered fastq files as output that you will want to use as input to your program 
kmerkit kextract --name test --workdir /tmp --samples A A.fastq.gz 
```
### CLI
```bash
# your program will take fastq files as input, or in the syntax here `--sample name fastqfile`
kassemble --name assembled --workdir /tmp-assembled/ --sample A A.fastq.gz
```

### Installation 
```bash
# conda install kmerkit -c conda-forge -c bioconda

# for now, do dev installation with pip
git clone https://github.com/eaton-lab/kmerkit
cd kmerkit
pip install -e .
``` 

### Description of user interaction:
The preferred way to run analyses in kmerkit is to use the API interactively in a jupyter notebook. This allows access to statistics, plotting summaries, and encourages users to create reproducible documentation of their workflow.

```python
import kmerkit  

# DATA
FASTQS = "/tmp/*.fastq.gz"
PHENOS = "/tmp/phenos.csv"

# get dict mapping {sample_names: [fastq_files]}
fastq_dict = kmerkit.get_fastq_dict_from_path(
    fastq_path=FASTQS, 
    name_split="_R",
)

# assemble kmers
kmerkit.Kassemble(
    name='test', 
    workdir='/tmp', 
    fastq_dict=fastqdict,
    kmersize=31,
    assemble_kmers="/tmp/kassemble_test",
).run()

```

### Related tools
My program...

Packages that will be used follow: 
`subproccess`: to run new applications or programs through Python code by creating new processes.\
`pandas`: to organize and analyze data.\
`toyplot`: to generate line plots.\
`loguru`: to bring enjoyable logging in Python.\
`kmc`: to count k-mers.\
`numpy`: to work with arrays and matrices to analyze data.\
`gemma`: to perform Genome-wide Efficient Mixed Model Association.\
`SPAdes`: to assemble denovo contigs. 
