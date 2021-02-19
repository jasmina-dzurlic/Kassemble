# Project: Kassemble 

### Description of project goal:
My program will assemble reference-free genome wide associations (GWAS) with a k-mer based approach. For the class project, I will build the `kassemble` module that will assemble unique k-mers into denovo contigs in order to map the location of genetic variants detected.  

Kmerkit is a general toolkit for performing reference-free genome-wide association analyses from kmers. `kassemble` will be a module part of the package that uses other modules in the package to create an assembly of a denovo contig. 

### Kmer kit
`kcount`: count unique k-mer reads present in a genome.\
`kextract`: extract reads from fastq files that contain target kmers.\
`kfilter`: filter unique k-mer reads based on statisical presences.\
`kgroup`: group unique k-mer reads with associated phenotypes.\
`kassemble`: assemble extracted k-mers into denovo contigs to map the location in a genome.\
`kmatrix`: use gemma to create a kinship matrix of unique k-mers.\
`kgwas`: run plink with genotype and phenotype data to detect GWAS.\
`klearn`: visualize sample/group genotype data (toyplot, scikit-learn etc.).

#### Installation with conda (coming soon)
```bash
# conda install kmerkit -c conda-forge -c bioconda

# for now, do dev installation with pip
git clone https://github.com/eaton-lab/kmerkit
cd kmerkit
pip install -e .
```

### Description of the code:
  
I will use multiple class objects for kassemble. For now, one class object will be to import fastq files with extracted unqiue k-mers.\
Another class object will be used to combine fastq files that contain unqiue k-mers to create denovo contigs of genetic variants.\
Another class object will be for producing plots and maps of location of contigs present in the genome.\
More class objects will be added as the project progresses...

Packages that will be used follow: 

`subproccess`: to run new applications or programs through Python code by creating new processes.\
`pandas`: to organize and analyze data.\
`toyplot`: to generate line plots.\
`loguru`: to bring enjoyable logging in Python.\
`kmc`: to count k-mers.\
`numpy`: to work with arrays and matrices to analyze data.\
`gemma`: to perform Genome-wide Efficient Mixed Model Association.\
`SPAdes`: to assemble denovo contigs. 

### Description of the data:
Kassembly will use genomic data in a .fastq format and phenotype data in a .csv format. 

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
