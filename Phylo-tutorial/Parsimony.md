# Cladistic methods: Maximum Parsimony

## The theory

The Maximum Parsimony method is based on the philosophical tenet known as *Occam’s Razor* or *lex parsimoniae*, proposed by the English monk William of Ockham in the 14th century, based on his readings of classic Greek philosophers. Its modern formulation is:

```
The simplest explanation is usually the correct one.
```

This principle has been often criticized, especially when applied to biological systems, which stubbornly oppose the laws of logic[^1]), because the correct explanation is not usually the simplest one.

In phylogeny, this principe was adopted as:

```
The shortest tree is usually the correct one.
```

The **length** of a tree is defined as the total number of substitutions that must have occurred along all its branches to generate the original data matrix.

We must be aware that Maximum Parsimony analyses are very sensible to the phenomenon known as **Long Branch Attraction (LBA)**, in which lineages with high substitution rates tend to group together in the tree, even if there is no real relationship between them. Ignoring this issue has led to the publication of some erroneous taxonomic conclusions, including some bizarre phylogenies showing than Guinea pigs are not rodents or that the hedgehog is the ancestral mammal. 

## Calculating the length of a tree

For each position in the matrix, we put in each terminal node its corresponding nucleotide. Then we reconstruct which nucleotide was present in each of the ancestral internal nodes:

-	If we have the same nucleotide in a pair of terminal nodes, then the nucleotide at their ancestral node is the same nucleotide.
-	If both nucleotides are different, we determine which one is the ancestral using one of the diverse parsimony algorithms (Fitch, Wagner, Dollo, Transversion...).

Once the whole tree is reconstructed, we count how many nucleotide changes happened along it.

We repeat the same process for each of the positions of our matrix, and at the end we add all the values to get the total length of the tree.

## Maximum Parsimony algorithm

Ideally, we could create all the possible trees, calculate the total length of each one, and choose the shortest tree.

But this is not feasible. The total number of possible trees (rooted) for a T number of taxa is given by this formula:

$$
N = (2T-3) \prod\limits_{i=3}^T (2i-5)
$$

This means that we have 105 possible trees for 5 taxa, more than 34 million trees for 10 taxa, and if we have more than 50 taxa the total number of possible trees is higher than the number of atoms in the entire Universe.

As it is not possible to build a computer bigger than the Universe, we must use different algorithms to be able to carry out a parsimony analysis:

- **Exhaustive search**: We build all the trees, iteratively. We start with three taxa, chosen randomly. Then, in each step, we add one more taxon to the tree, in every possible position, and continue this process recursively (Figure 5). This method ensures that we will find the shortest tree, but it is only feasible for very small datasets (maximum 10 taxa).
- **Branch and bound**: Identical to the exhaustive search, but including a length threshold. Every time that we add a taxon, we calculate the length of the trees, discarding those whose length is higher than the threshold. This greatly reduces the number of trees, and still ensures that we will find the shortest tree, but it is still unfeasible for large datasets.
- **Heuristic search**: There are different approaches for this algorithm.
  - **Stepwise addition** is identical to branch and bound, but it only keeps the shortest tree in each iteration.
  - **Star decomposition** is more complex, because in each step it collapses the tree and performs a series of complex operations as it “unfolds” the tree. At the same time, it rearranges the tree in each step and calculates the new length, sometimes finding shorter trees that it may have overlooked in previous steps.
  - There are different rearrangement (or **branch-swapping**) algorithms; the most common is tree bisection and reconnection (**TBR**). This is the fastest tree search algorithm, but it does not guarantee finding the shortest tree, even using branch-swapping methods.

## Consensus tree

When an analysis (not only Maximum Parsimony, but also Bayesian Inference or any other kind) produces a series of trees as a result, we must create a consensus tree. This may happen in a Maximum Parsimony search finds that, instead of a minimum-length tree, we have more than one tree that share the same minimum length.

There are several methods for creating the consensus tree. Some of the most common are:

-	**Strict**: The consensus tree only shows the nodes that are present in all the trees.
-	**Majority Rule**: The consensus tree only shows the nodes that are present in a predefined percentage of the trees.




[^1]: As Ian Malcolm (Jeff Golfblum) said in Jurassic Park, “life finds a way”.
