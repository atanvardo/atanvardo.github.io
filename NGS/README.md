# NGS for dummies

This is a tutorial for the pipeline that we follow for NGS data in our lab. 

## Wet lab

### Basics

Illumina is a high-throughput sequencing by synthesis. What does this mean?

-	**High-throughput**: it’s going to sequence a lot of DNA fragments at once.
-	**By synthesis**: the machine will determine which nucleotide is at a particular position by synthetizing the complementary chain, and detecting the light emitted by the new nucleotide when it is inserted.

Yes, we are going to sequence **all our samples** (specifically, their COI fragments) in a single batch.

Here it is explained how our primers with tags work and their structure:

- [Primers and tags](/Primers.md).

Here we give an example of how to design our plates and organize the primer combinations:

- [Plate design for the Sonata project](/Plates.md).

### PCR

Check the [lab protocol page](/Labprotocol.md).

### Equimolar pooling

After running the PCR, we need to mix all the PCR products in a single pool, but including the same amount of DNA from each of them. In order to do this, we need to know the DNA concentration in each PCR product. We take the measurements using a Qubit, and then calculate how much volume of each PCR product we need to take to get 100ng of DNA (just divide 100 by your concentration in ng/uL).

### Sequencing

When all the PCR products of our plates have been mixed in a single pool, it's ready to be sent to the sequencing service for its transformation into an Illumina library and sequencing. Here are some details about the sequencing process and the output:

- [Sequencing](/Sequencing.md).

## Bioinformatics

### Pre-requirements

All the commands and scripts are run in a Linux environment. You should be familiar with how to work in Linux and move through folders and executing commands.

- If you are using a Windows computer, install the Windows subsystem for Linux ([Instructions](/WSL.md)).

- Install the [pre-required packages](/Prerequirements.md).

### Folder structure

This guide will use the folder structure that I used when writing the scripts for the first run of our analyses for the Sonata project:

- Project directory
	- `coidb`
	- `sequences`
		- `01-demultiplexed`
		- `02-quality_control`
		- `03-unmerged`
		- `04-merged`
		- `05-qc_filter`
		- `06-fasta`
		- `07-blast`
		- `08-definitive`
		- `09-trimmed`

The folder named `coidb` contains our reference database. In order to create the database, we will go to GenBank and download all the sequences corresponding to our target taxonomic group and marker, in a single fasta file. Then, in that folder, we will run this command:

```
makeblastdb –in [name_of_our_fasta_file] –dbtype nucl
```

You can change the names of files and folders, but remember to always check the scripts and modify them accordingly!

### Step by step

Step 1: [demultiplexing](/Demultiplexing.md).
