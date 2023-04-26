# Distance-based phylogenetic methods

## UPGMA

This method, developed by Sokal and Michener in 1958, was the first phylogenetic algorithm. It is very straightforward: it reconstructs the tree hierachically from a simple distance matrix.

These distances can be calculated using different indices. One of the simpler and most well-known is Jaccard index, which divides the number of different positions between two sequences by the total number of positions:

$$
J(A,B) = \frac{|A \bigcap B|}{|A \bigcup B|}
$$

The algorithm starts taking the two taxa with the least distance, draw them in the tree, and replace them in the matrix by a mixed new taxon. The process is repeated until all the taxa are drawn in the tree.

## Neighbor-joining

This is an upgraded version of UPGMA, developed by Saitou and Nei in 1987. Is a more complex method, as the distances between sequences are corrected using a nucleotide substitution model. Additionally, the tree is not created from the distance matrix, but from something called **Q matrix** that is created by complex calculations from the distance matrix.

Its main advantages are that it is extremely fast and it does not require much computing power. On the other had, it is not very reliable and it is very sensible to artefacts. Thus, it is used to have a rough idea of the relationships between the analyzed organisms before moving on to more complex and reliable analyses. Some advanced algorithms use Neighbor-Joining to create the starting tree that they require.

