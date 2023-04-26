# Tutorial: Maximum Likelihood with IQTREE

IQTREE is one of the most recent incorporations to the zoo of phylogenetic programs. It is able to run Maximum Likelihood analyses very fast, which is very useful when we are analyzing big matrices, specially in phylogenomics.

## Downloading and running IQTREE

IQTREE can we downloaded from [its website](http://www.iqtree.org/), We will get a zip file that can be unzipped.

The IQTREE executable is inside the `bin` folder. There are two executables inside that folder:

- `iqtree.exe`: This is the proper IQTREE program.
- `iqtree-click.exe`: This program is some kind of interface to IQTREE where we can introduce the parameters one by one.

Be aware that IQTREE is a program that does not have graphical interface. It should be called from the command line, including all the parameters in a single line.

It is advisable to put all the files (our data matrix and any supplementary file) in the same folder as the IQTREE executable.

One easy way to run the command line directly in that folder in Windows is going to that folder in Windows Explorer. Then, we keep pressed the `shift` key, and right-click on any empty space inside the folder. In the contextual menu, we will see, depending on our system, the option `Run command line here` or `Run PowerShell here`. We can click on either of them.

In the command line window, we will have to write the name of the program (`iqtree.exe` or `iqtree2.exe`, depending on the version that we downloaded), and then the list of all the parameters that we want to use. For example:

```
iqtree2.exe -s .\GU_NG.nex -p .\GU_NG.partitions.txt -m GTR+I+G -bb 10000
```

In this example, we are:

- Using the `-s` parameter to tell IQTREE which file contains our data, in this case the file called `GU_NG.nex`.
- Using the `-p` parameter to tell IQTREE which file contains the information about the partitions included in our data, in this case the file called `GU_NG.partitions.txt`.
- Using the `-m` parameter to set the model to `GTR+I+G`, i.e. the General Time Reversible model including the proportion of invariant sites and a gamma distribution.
- Using the `-bb` parameter to run an ultrafast bootstrap approximation (UFBoot) analysis to get the support values for our tree, in this case with `10000` replicates.

The list of all parameters and their options can be found in the extensive [documentation](http://www.iqtree.org/doc/).

## Model testing

IQTREE includes its own model testing function. One of its advantages over jModelTest is that it has an option to check if different partitions can share the same model, reducing the number of parameters of the analysis and thus increasing its speed.

In order to run this model testing tool just before the analysis, we should just include this option for the model parameter: `-m MFP+MERGE`.

## Partitions file

If our dataset includes more than one partition, we should include this information in a plain text file and load it with the `-p` parameter.

This file includes a line for each partition, indicating the type of data, the name of the partition, and which nucleotides it includes:

```
DNA, 18S = 1-828
DNA, 28S = 829-1621
DNA, ITS2 = 1622-2096
```

We can also separate the codons of a coding fragment:

```
DNA, COIcodonpos1 = 1-792\3
DNA, COIcodonpos2 = 2-792\3
DNA, COIcodonpos3 = 3-792\3
```
