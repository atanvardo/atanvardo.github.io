# Preparing your files

## Pre-requisites

This tutotial assumes that you have already edited your sequences and made a separate alignment for each of your markers.

It also assumes that you are working with Geneious. Your should make a folder in which you will import your alignments.

## Check the names of the sequences

Unless you are doing some really special analysis, or something really stupid, the names of the sequences obtained from the same specimen should have exactly the same names in each alignment.

For example, if you have two alignments corresponding to two markers (let's say 18S and COI) that look like this:

18S:
```
Specimen_1_18S	CGATCGATGCGACA
Specimen_2_18S	CGACCGAA-CGACA
```

COI:
```
Specimen_1_COI	CGCGATCATGCATG
Specimen_2_COI	CGCGATAATGCTTG
```

Notice that the names of the sequences are not identical. In this case, when we concatenate them to create the full matrix, we'll get this:

```
Specimen_1_18S	CGATCGATGCGACA--------------
Specimen_2_18S	CGACCGAA-CGACA--------------
Specimen_1_COI	--------------CGCGATCATGCATG
Specimen_2_COI	--------------CGCGATAATGCTTG
```

If we give them the same names...

18S:
```
Specimen_1	CGATCGATGCGACA
Specimen_2	CGACCGAA-CGACA
```

COI:
```
Specimen_1	CGCGATCATGCATG
Specimen_2	CGCGATAATGCTTG
```

...we will get the correct matrix:

```
Specimen_1	CGATCGATGCGACACGCGATCATGCATG
Specimen_2	CGACCGAA-CGACACGCGATAATGCTTG
```

## Check the names of your sequences (again)

Sequence names should not have any characters besides:

- Letters (`abCD`...)
- Numbers (`1234`...)
- Underscores (`_`)

Be specialle aware of dots (`.`), as they can be dangerous. Some phylogenetic programs interpret them as a `same nucleotide as above` character and this can lead to errors or (worse) reading your matrix incorrectly.

## Create the concatenated alignment

In Geneious, it is very easy. Just select the alignments that you want to concatenate, and on the top menu click on `Tools` > `Concatenate sequences or alignments...`.

It will ask us in which order we want the markers. It doesn't really matter which order we choose, but please be sure to take note of it.

## Save your file

Select your concatenated alignment, and export it as a Nexus file. And it should be ready to be used by any phylogenetic software without any problem.

## Include the positions of each marker

This must be done manually, unfortunately.

First, check the order in which you concatenated the markers, and the length (in base pairs) of each one. For example:

```
18S		851
28S		658
COI		715
ITS		431
```

The first marker (18S) will start in the nucleotide 1, and end in the nucleotide 851. The marker 28S will then start in the nucleotide 852 (the next one) and finish in the nucleotide 1509 (851 + 658). An so on:

```
18S		1 - 851
28S		852 - 1509
COI		1510 - 2224
ITS		2225 - 2655
```

Take note of this information. You will include it in different ways depending on the program that you will use for your analisis. For example:

- MrBayes: Set the partitions as it is shown in the [MrBayes tutorial](/T-MrBayes.md).
- IQTREE: Create a partitions file as it is shown in the [IQTREE tutorial](/T-IQTREE.md).
- BEAST: Include the information as an `assumptions` block in your nexus file, as show in the [lesson about data files](/Data_files.md).

For programs like IQTREE or MrBayes you want to separate the different positions in coding fragments to create separate partitions. This is usually codified like this (but check because it may vary depending of which program you use):

```
18S		1 - 851
28S		852 - 1509
COIpos1		1510 - 2224\3
COIpos2		1511 - 2224\3
COIpos3		1512 - 2224\3
ITS		2225 - 2655
```
