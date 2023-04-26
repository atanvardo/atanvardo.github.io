# Bayesian Inference

## The theory

Bayesian Inference calculates the probability of a hypothesis ( $H$, our tree) given some starting data ( $D$, the matrix). Is the complete opposite of likelihood, and it is calculated using the **Bayes theorem**:

$$
P(H|D) = \frac{P(D|H)P(H)}{P(D)}
$$

It is a **posterior** probability calculation, while likelihood is anterior probability. We can see the difference with this simple example:

-	Anterior probability (Likelihood): We have a box with two green balls and three blue balls. *What is the probability of drawing a blue ball?*
-	Posterior probability (Bayesian): We have a box and we draw a blue ball. *What is the probability of that the box contains two green balls and three blue balls?*

The meaning of the components of the Bayes equation for phylogenetic analyses is:

-	$P(D|H)$: It is simply the tree likelihood. We already know how to calculate it (just using the Maximum Likelihood algorithm).
-	$P(H)$: It is the probability of getting a particular tree randomly when sampling all the possible trees. It is usually considered to be equal to $\frac{1}{N_{trees}}$, but some experts have some doubts about it.
-	$P(D)$: It is the probability of our matrix, i.e. that for each position in the sequence of each of the taxa we can find those particular nucleotide instead of another. This value is absolutely impossible to calculate. In order to be able to carry out this analysis, we should use a smart trick to remove this element from the equation. We will learn how to do it in the next section.

## Bayesian Inference algorithm

This method uses a **Markov chain Monte Carlo** algorithm. This procedure is equivalent to “have a walk” around a multidimensional space conformed by all the possible trees. It starts in a random place and looks which tree is at that position ( $T_{former}$ ). Then it takes a step, moving to a close place (by modifying a bit any of the parameters of the tree) and look at the tree that is there ( $T_{new}$ ). And then it calculates the ratio between the Bayesian probabilities of both trees:

$$
R = \frac{T_{former}}{T_{new}}
$$

Unfolding the Bayes equation to its full form:

$$
R = \frac{\frac{P(D|H_{new})P(H_{new})}{P(D)}}{\frac{P(D|H_{former})P(H_{former})}{P(D)}}
$$

And now we can do the trick! The element that can't be calculated, P(D), is present in both the numerator and the denominator, so we can simply remove it:

$$
R = \frac{P(D|H_{new})P(H_{new})}{P(D|H_{former})P(H_{former})}
$$

Additionally, we said that the probability of each tree, $P(H)$, is (in theory) the same in all the cases. So we can also remove it, and then we find that…

$$
R = \frac{P(D|H_{new})}{P(D|H_{former})}
$$

The ratio between the Bayesian probabilities of both trees is simply the ratio between their likelihoods! So, in the end, doing a Bayesian Inference analysis is equivalent to doing a bit more sophisticated Maximum Likelihood analysis.

If $R > 1$, we discard the former tree, and start walking from the new tree. If $R < 1$, we go back to the former tree and try to find another path.

BUT, the aim of the analysis is not to find the tree with the highest likelihood. Every certain number of steps, the cold chain saves its tree to a list. Once the walk is over, the first trees, saved when the chains were starting to explore, are removed (burn-in). Then some programs (like MrBayes) create a consensus tree from all of them, while others (like BEAST) take the tree with highest likelihood, and then they calculate the posterior probability of each node.

## Posterior probability

The Bayesian Inference is a slow process that requires a high amount of computer power. A typical analysis may take hours or even days. Thus, it is not feasible to perform a bootstrap test to calculate the reliability of the nodes: a normal analysis that takes 8 hours will need 9 years to do 10,000 bootstrap replicates!

Thus, Bayesian Inference analysis use an alternative test based on calculating the posterior probabilities of each node, based on the values of the parameters and the trees that the analysis has been sampling. This value can act as support values for them.

Posterior probability is not equivalent or comparable to bootstrap. It is also more strict: it is considered that posterior probability starts to indicate an acceptable support if its value is higher than 90%.

In spite of everything, posterior probability values from a Bayesian Inference analysis are usually considered to be more reliable than the bootstrap values from Maximum Likelihood methods.
