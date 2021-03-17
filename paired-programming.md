# Git Collab Assignment

## Goal of the project: Is it clear to you from the proposal.md how the goal can be accomplished using Python and the specified packages?
The goal of this project is to assemble contigs from k-mers. This will be accomplished using an already existing package, Spades, that can be used only on CLI. It is clear to me that this can be accomplished using python, subprocess, and spades in conjunction with the tools being developed in kmerkit. 

##The Data: Is it clear to you from the proposal.md what the data for this project is, or will look like?
The input data for this program was described as both some output from previous steps of kmerkit and also as a fasta file. Will the output of the previous kmerkit steps be a fasta file? In the SPAdes documentation, they show how different types of sequencing results can be used as inputs. Will kassemble assume a single type of sequencing data (i.e. Illumina)? Will it matter?

##The code: (Look at the Python code files in detail first and try to comprehend a bit of what is written so far)

### Does the current code include a proper skeleton (pseudocode) for starting this project?
There is a good skeleton for the class object that explains in detail the inputs and what they should be. It would be nice to have some pseudocode for more expected functions inside the class function that have descriptive docstrings, just so that we can see the step-by-step plan and what you've already thought about. 

### What can this code do so far?
So far, this code imports SPAdes and other dependencies and has begun to use subprocess to run SPAdes. 

### Given the project description, what are some individual functions that could be written to accomplish parts of this goal?
Some functions (which Jasmina and I discussed together) that will be included in this project are:
	* a function that calls subprocess to run spades
	* a function that allows for visualization of contig assembly

Some functions that might be good to include:
	* If the data is not in the correct format to be input into SPAdes, then there could be a function that parses the data into the correct format
	* Will kassemble do anything with any of the normal SPAdes output files?

### Code contributions/ideas: 
I added some comments in Kassemble.py for running subprocess, and created some pseudocode for the visualization function that Jasmina wants to include in the kassemble class object. I kind of mentioned this above, but my biggest question after going through SPAdes documentation is what will the format of the data coming from upstream kmerkit functions be and will you need to specify in your SPAdes command what type of sequencing it is? Is there a single SPAdes command or will you need to pipe the outputs of several commands into others? If so, maybe it makes sense to write all the commands up front (e.g. cmd1, cmd2, cmd3, etc.) and then call subprocess on those commands. If not, will you have downstream functions that do something to one of the files in the SPAdes output folder? What function will that be?