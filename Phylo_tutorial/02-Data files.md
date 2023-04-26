# Data files

When we codify the data that we gathered to reconstruct a phylogenetic tree (usually DNA sequences, but sometimes other kind of data), those are usually codified in one of the standard file format. Choosing one or another file format depends on our data and the program that we are going to use, as not all the programs are compatible with all the formats. The most used file format is NEXUS, due to its versatility.

## PHYLIP format

It was the first standart format to give data to phylogenetic programs. It was developed by Joe Felsenstein in 1980, when he created his phylogenetic package PHYLIP, the first software dedicated for reconstructing phylogenies. Indeed, most of the current phylogenetic programs are based on the PHYLIP source code (which is still being updated), so they can be considered as its "children".

The PHYLIP format is a simple text file. In the first line we indicate the number of taxa and the number of characters. This line is followed by the matrix, in which each line includes the name of the taxon (the strict PHYLIP format uses the first 10 characters of the line for this, so if our name has a length of 6 characters we must add 4 blank spaces afterwards), followed by its corresponding sequence.

```
8    6
Alpha1    AAGAAG
Alpha2    AAGAAG
Beta1     AAGGGG
Beta2     AAGGGG
Gamma1    AGGAAG
Gamma2    AGGAAG
Delta     GGAGGA
Epsilon   GGAAAG
```

The PHYLIP format requires that the sequences have the same length are must be aligned.

Files in PHYLIP format usually have the extension phy.

## FASTA format

This format was developed by Lipman and Pearson in 1985. It is a simple text format that stores a collection of sequences. It does not require that the sequences are aligned, have the same length, or even have any relationship between them, so it is used as a "storage". Each piece of data includes two lines: in the first line we write the name preceded by the character `>`, and in the second line we include the sequence:

```
>Seq1
ATCGATCGGACGATCGATGCATCGACTG
>Seq2
AGCTAGCTACGATGCATTCGATCGATGCATCGATGC
>Seq3
ACGGACTCGTAGCAGCGACGGAGCATGCATCG
```

Recently, Illumina has created an improved version, FASTQ, which includes information about the sequence quality. It has not yet been implemented in phylogenetic programs (it has other uses), but may be used in the future.

## MEGA format

This is the format developed by Kumar, Tamura and Nei for their program MEGA. It is similar to FASTA, but using the symbol `#` instead of `>`. It must have a heading composed by the line `#Mega` at the beginning, and one or more of optional comments below it:

```
#Mega
Title: this_is_a_test

#168
ACTGATCGATCGATCGATGCACGCG
#169
GACTGATCGATGCTAGCTGACGATC
#171
ACGTAGCATGCTAGCTGATCATGCT
#176
GACTGACTGACTACTGCTGATGCTA
#199
ACGTCAGATGATCGATGTAGCATCG
```

Unlike the FASTA format, the MEGA format requires that the sequences are aligned and have the same length.

## NEXUS format

This is the most commonly used file format due to its flexibility and standardization. In this case, the text file starts with the line `#NEXUS`, followed by a series of blocks.

Each NEXUS block starts with the word `begin` followed by the name of the block, and ends with the word `end`. Each line ends with a semicolon (`;`). The definition of the blocks and all the possible commands are detailed in the original paper[^1], although some phylogenetic programs admit and can interpret their own blocks.

The most basic block is the `data` block, designed to include the data matrix. It includes a series of lines that define the characteristics of the matrix (size, type of data, special symbols, etc), followed by a line that only includes the word matrix, and finally the matrix. The names of the sequences are separated from the data by a tabulator[^2]:

```
begin data;
dimensions ntax=6 nchar=8;
format datatype=dna missing=? gap=-;
matrix
Taxon1	AGCCGTTA
Taxon2	AGTCGT??
Taxon3	AGCCATTA
Taxon4	GGGCGTTA
Taxon5	AGCCG--A
Taxon6	AGCCG--A
;
end;
```

Sometimes, this block is separated in two: the `taxa` and `characters` blocks. This happens, for example, in the files exported by Geneious. Personally, I dislike this separation, as I found it redundant, buy anyone can format the files as mostly pleases them.

Another useful block is the `assumptions` block, which allow us to define partitions in our matrix. This is necessary if our matrix is formed by various concatenated fragments. Some programs will recognize this block, and will independently calculate the values of their parameters for each of the partitions, producing more reliable and correct results. Other programs will not read it, and we will have to introduce the partitions using different systems.

```
begin assumptions;
charset fragment1 = 1-450;
charset fragment2 = 451-893;
charset fragment3 = 894-1432;
end;
```

This block is also useful if we want the program to analyze separately the third codon in coding genes, the loops of ribosomal RNAs, introns, etc.

Some programs (for example, MrBayes) define their own blocks, which include specific instructions that are exclusively interpreted by them.

## NEWICK format

This format is used to store the phylogenetic trees. The name comes from a seafood restaurant called Newick, in Dover (New Hampshire), in which James Archie, William H. E. Day, Joseph Felsenstein, Wayne Maddison, Christopher Meacham, F. James Rohlf and David Swofford shared a casual dinner while discussing this issue.

This format represents each node using parentheses, including inside them the *children* nodes separated by commas. At the end there is a mandatory semicolon.

For example, a simple tree composed only by two taxa, A and B, will be written as:

```
(A,B);
```

The parentheses are nested in the same way as the clades in the tree. For example, in the following case, A is a sister taxon of B, and both of them form a clade which is sister to the taxon C. The groups formed by A, B and C is a sister clade of the clade formed by D and E:

```
(((A,B),C),(D,E));
```

Additionally, we can include information such as the branch lengths, adding the value after a colon written at the end of each node:

```
(((A:0.01,B:0.02):0.11,C:0.13):0.23,(D:0.09,E:0.07):0.45);
```

Some programs add more information within brackets, which can cause problems when we import the file into another program. For example, BEAST stores in this way data about the confidence intervals for the node heights, the evolutionary rate of each fragment at each node, and many other parameters.

### Trees in NEXUS format

Trees can also be stored in NEXUS format (see above). In this case, the NEXUS format will include a `trees` block, in which one or several trees will be stored in NEWICK format.

```
begin trees;
tree NAMEOFTHETREE = (((A:0.01,B:0.02):0.11,C:0.13):0.23,(D:0.09,E:0.07):0.45);
end;
```

[^1]: Maddison, D.R., Swofford, D.L., Maddison, W.P. (1997). NEXUS: An extensible file format for systematic information. Systematic Biology 46(4):590-621.
[^2]: Some programs, when they create NEXUS files, they use spaces or line breaks, which can cause problems when other more strict program reads the file.
