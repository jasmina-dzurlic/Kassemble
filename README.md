# Project: Kmerkit / Kassembly module 

An outline of a new project idea (for now)


### Description of project goal:
My program will provide both a API and CLI interface for detecting genome wides associations (GWAS) with a k-mer based anaylsis. For the class project, I will build the `kassemble` module that will assemble unique k-mers into contigs in order to map the location of genetic variants detected.  

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
