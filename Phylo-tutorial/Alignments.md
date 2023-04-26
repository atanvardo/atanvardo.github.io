# Alignments

There are several methods for aligning our sequences in order to create our matrix:

1. Classical alignment methods (Clustal, **ClustalW**, T-Coffee): They create a guide tree using the unaligned sequences, and start to create the alignment adding sequences in the order in which they appear in the tree. They define some values for “gap opening cost” or “gap extension cost” which modify the behaviour of the algorithm when it has to decide whether it should add gaps or not. They are very fast and work perfectly for coding markers, but they usually produce errors in other genetic fragments.
2. Iterative methods (PRRN/PRRP, DIALIGN, **MUSCLE**): Identical to the previous, but every time that they add a sequence they check the other unaligned sequences to check for artefacts. They optimise the alignment by iteratively calculating the distances between the sequences.
3. Phylogeny-guided methods (PRANK, PAGAN): They build a phylogenetic tree in each step (usually using Maximum Likelihood) to optimize the process. 
