# Phylogenetic support

How do we know if our tree is a truthsworthy representation of the relationships between the organisms that we are studying? The only information that we have is our dataset, there are no external data that we can use to calculate how reliable is our tree. But we can use a smart trick.

## Bootstrap

Bootstrapping is a method can let us know how reliable are the nodes of our tree. The name comes from the English idiom *"to pull oneself up by one's bootstraps"*, which approximately means that you should be able to do it which whatever you have.

This method follows this protocol:

1. The analysis is run with the original matrix, and we get a tree.
2. We create replicates of the original matrix, in which the positions are randomly shuffled.
3. For each replicate, we repeat the analysis with the same parameters, producing many trees.
4. For each node of the original tree, we check in how many of the replicate trees we recover that node. The obtained value (in percentage) is the bootstrap value for that node.

It is considered that a node is reliable if its bootstrap value is greater than 50%. Obviously, the more closer to 100% the better.

## Other support values

Some methods are unable to produce bootstrap values, for example Bayesian inference algorithms (we will see why later). They have their own ways of determining the reliability of a tree, for example by calculating the **posterior probability** of their nodes.

