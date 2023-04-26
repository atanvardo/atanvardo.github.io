# Dating phylogenies

There are several methods to **calibrate** a phylogenetic tree, so the length of its branches is proportional to the time between each pair of divergence events. It is advisable to use all possible methods, whenever the circumstances allow it.

## Events: fossils and biogeography

We can use fossils and biogeographic events to establish the ages of branches and nodes. Nevertheless, depending on the kind of event, we will use different methods to determine its minimum or maximum age.

When we set these calibrations points in a phylogenetic software, for example BEAST, we must create a probabilistic distribition from which the program will get values for the ages of the clades, which will include parameters such as a mean, a standard deviation, maximum and minumum values, etc. In order to set these parameters, we must keep in mind how we can interpret these events and how we can infer the age of our clades from them: 

| Method | Background | How to calculate |
| ---- | ---- | ---- |
| Fossils | We know the age of a fossil that can be assigned to a clade. | **Lower bound**: The age of the basal branch of the clade must be older than the age of the fossil. |
| Vicariance | Two sister clades are geographically separated, and we have some insight about which event separated them. | **Fixed time**: The age of the node when the separation occurred is the age of that event. |
| Archipelago | We know that the branches within a clade have been splitting as new island were formed in an archipelago. | **Upper bound**: The age of a clade composed by taxa native to an island must be younger than the age of that island. |

## Molecular clock

If we do not know any fossil or biogeographic event, we can use the **substitution rate** of the genetic fragment that we are using (its value is usually given in substitutions per site per million years) to calculate the age of each node. If we don't know the value of this rate for our organisms, we can use rates calculated for related taxonomic groups, but keep in mind that this method should be used with care, and we must check if the obtained ages make sense or not.

There are two different types of molecular clocks:

-	**Strict clock**: The rate is the same for each branch, and it is invariable. This is actually unrealistic, but analyses with a strict clock are usually faster and the resulting tree usually has higher support values.
-	**Relaxed clock**: It allows the rate to vary along the branches and the time. It is more realistic, but the analyses take longer and lose a bit of reliability.
