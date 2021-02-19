# Project: Kmerkit _ kassembly module 

An outline of a new project idea (for now)


### Description of project goal:
My program will detect and assemble genome wides associations (GWAS) with a k-mer based approach. For the class project, I will build the `kassemble` module that will assemble unique k-mers into contigs in order to map the location of genetic variants detected.  

Kmerkit is a general toolkit for performing reference-free genome-wide association analyses from kmers. It uses KMC to count and filter kmers, and has options to perform associations using gemma. The preferred way to run analyses in kmerkit is to use the API interactively in a jupyter notebook. This allows access to statistics, plotting summaries, and encourages users to create reproducible documentation of their workflow.

#### Installation with conda (coming soon)
```bash
# conda install kmerkit -c conda-forge -c bioconda

# for now, do dev installation with pip
git clone https://github.com/eaton-lab/kmerkit
cd kmerkit
pip install -e .
```


### Kmer kit
`kcount`: ...
`kextract`: ...
`kfilter`: ...
`kgroup`: ...
`kassemble`: ...
`kmatrix`: ...
`kgwas`: ...

### Description of the code:

(It's fine to say you are not sure yet...)  
I will one class object for extracting data from online, and another class object for analyzing the data and producing plots.
list any packages you can find online which you may use:  

`subproccess`:
`pandas`: to organize and analyze data.  
`toyplot`: to generate line plots.  
`loguru`: ...
`kmc`: ...
`numpy`: ...

### Description of the data:
I will access data programatically from a public online database using a REST API framework. 

### Description of user interaction:
Example: user could call the program from the CLI and it will open either report the results as text to the terminal, or if the user requests a plot, it will open the default browser and display.
```
# example command line interface
my_weather_program --city "New York" --state NY --mean-temp --date-range 1900 2021
```

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

# count kmers
kmerkit.Kcount(
    name='test', 
    workdir='/tmp', 
    fastq_dict=fastqdict,
    kmersize=31,
).run()

# find kmers unique to one group versus another
kmerkit.Kfilter(
    name='test', 
    workdir='/tmp', 
    phenos=PHENOS,
    trait='trait',
    mincov=0.25,               # must be present in 25% overall
    mincanon=0.25,             # must exist in both forms in 25% of samples where present.
    minmap={1: 0.5, 0: 0.0},   # must be present 50% in group 1
    maxmap={1: 1.0, 0: 0.0},   # must be absent in group 0
).run()

# get fastq reads filtered to only those matching target kmers
kmerkit.Kextract(
    name='test',
    workdir='/tmp',
    fastq_dict=fastq_dict,
    group_kmers="/tmp/kgroup_test",
).run()  

# get matrix of (nsamples x nkmers) as geno data, from Kfiltered kmers.
kmerkit.Kmatrix(
    name="test",
    workdir="/tmp",
    ...
)
```
