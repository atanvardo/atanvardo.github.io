# Tutorial: Bayesian Inference with MrBayes

MrBayes is a program that was created by John Huelsenbeck and improved by Fredrik Ronquist. It builds phylogenetic trees using a simple Markov chain Monte Carlo algorithm.

It is a command line program, without graphical interface. But it is very simple. It can be used in two ways:

- Interactively, in which we will introduce the commands one by one in the MrBayes command line.
- Including all the commands in a MrBayes block in the input NEXUS file.

Personally, I prefer the first way, but most of the people prefer the second. This tutorial will follow my preferred workflow, introducing the commands one by one in the command line.

In this tutorial we will follow the steps to carry out a simple analysis to learn its workflow. For more complex analyses, feel free to read its complete manual.

## Downloading MrBayes

MrBayes can be downloaded from [its website](http://nbisweden.github.io/MrBayes/download.html). In that page, these is a link to pre-compiled executables ready for Windows.

As usual, it will be downloaded in a compressed folder that can be unzipped. The MrBayes executable is in the `bin` folder inside.

There are two versions of the MrBayes executable, one for 32-bit systems and another for 64-bit systems. Any moder computer is a 64-bit system, which can run both versions, but it is always advisable to run the 64-bit executable.

## Starting MrBayes

MrBayes is a command line program, but interactive. This means that we can run it simply by double-clicking the executable, and it will show a command line window in which we will be writing a series of commands.

The first thing to do is loading our data. MrBayes requires our matrix in NEXUS format. In order to load it, we write the command `execute` followed by the name of our file. It is advisable to put the file in the same folder as MrBayes. For example, if we want to load the file called `cox1.nex` we must write:

```
execute cox1.nex
```

If we decided to include a MrBayes block in the NEXUS file, MrBayes will start to automatically run all the commands that we included there. If not, it will show the list of taxa in our matrix and wait for us to introduce manually the commands.

## Partitions

If our dataset includes partitions, this is the moment to set them. In order to describe the partitions, we use the command `partition`, followed by the name of our partition scheme, an equal sign, the number of partitions, a colon, and the nucleotide ranges for each partition. For example:

```
partition partexample = 3: 1-423, 424-679, 680-901
```

And then we tell MrBayes to use this partition scheme using the command `set`:

```
set partition = partexample
```

## Setting the model

Now we must choose the best nucleotide substitution model for our data, which we should have calculated previously using tools such as jModelTest.

We use the command `lset` to specify the model. This command has two options:

- `nst`: It indicates the number of substitution categories in our model. Remeber to check the **![table of nucleotide substitution models](https://github.com/atanvardo/Phylo-Tutorial/blob/main/04-Nucleotide%20substitution%20models.md#table-of-nucleotide-substitution-models)**! In MrBayes, it can have one of the following values:
	- 1: Jukes-Cantor model.
	- 2: Hasegawa-Kishino-Yano model.
	- 6: General Time Reversible model.
- `rates`: It indicates the extra parameters that we want to include in the model. It can have one of the following values:
	- `equal`: No extra parameters.
	- `propinv`: Includes the proportion of invariant sites.
	- `gamma`: Includes a gamma distribution.
	- `invgamma`: Includes both.

For example, to set the model to GTR+I+G, we must write:

```
lset nst=6 rates=invgamma
```

These are actually the default values for these parameters, so we can omit this step if this is the most appropiate model for our dataset.

If we have more than one partition, we must specify to which of them we are applying the model:

```
lset applyto=(1,3) nst=6 rates=invgamma
```

## Running the chains

Once the model is set, we can start the analysis. Before starting the Markov chain Monte Carlo, we must consider:

- How many *steps* (generations) are we going to run the analysis. It is advisable to run at least 1 million, and preferably 10 million. But this number will vary depending on our data. We will see later how to check if the number of generations that we chose was adequate.
- Every how many generations MrBayes is going to sample a tree. We should aim to have 10000 trees at the end of our analysis, so this number will be the number of generations divided by 10000. We must remember that the trees will be stored in a file that can grow to ludicruous sizes if we set this parameter to sample every few generations or if we extend the analysis for many millions of generations.

We use the command `mcmc` as follows (in this example, setting 1 million of generations, and sampling one tree every 100 steps):

```
mcmc ngen=1000000 samplefreq=100
```

The analysis will start immediately. After some starting calculations, the program will show the progress with some information displayed in columns with numbers:

```
       0 -- [-40280.916] (-40083.079) (-40318.476) (-40214.391) * [-40058.704] (-40097.731) (-39972.676) (-39572.487)
    1000 -- (-34313.218) (-33891.456) (-33912.809) [-33546.700] * [-33408.320] (-33630.662) (-33553.613) (-33809.245) -- 0:49:57
    2000 -- (-33469.023) (-33186.725) (-33016.983) [-32915.213] * [-32712.362] (-33030.697) (-32848.663) (-32981.443) -- 0:49:54
    3000 -- (-33023.709) (-33049.196) (-32759.630) [-32470.896] * [-32550.191] (-32721.586) (-32599.931) (-32604.505) -- 0:49:51
    4000 -- (-32770.179) (-32988.013) (-32708.005) [-32422.309] * (-32397.086) (-32586.534) (-32560.640) [-32330.405] -- 0:49:48
    5000 -- (-32646.850) (-32836.190) (-32697.559) [-32392.402] * (-32262.687) (-32555.884) (-32538.766) [-32259.005] -- 0:49:45
```

We can see that there are two sets of columns, separated by asterisks. Each group corresponds to a separate analysis, because MrBayes is actually running TWO parallel analyses (*runs*) at the same time. Why? We will see later. We can set how many runs we want to do (read the manual if you want to know how); the default value is 2.

Within each run, there are four columns, corresponding to the four *chains*. Each of the runs sample the tree space using these chains, following this algorithm:

- One is the cold chain, which corresponds to the chain that found the most probable tree. This chain samples trees that are very close, just making small changes to the tree that it is holding at that moment.
- The other three chains are hot chains, and make big jumps across the tree space, evaluating random trees that can be very different to the most probable tree found until that moment. If one of the hot chains finds a better tree, it becomes the cold chain, and the previous cold chain becomes hot.

MrBayes displays the 'position' of the chains showing the probability (likelihood) of the tree that each of them is holding. That value is surrounded by square brackets in the cold chain, and by parentheses in the hot chains.
During the first generations, it is normal that the cold chain changes repeatedly from one column to another, because the analysis still has not found the area where the most probable trees are located.

Every several generations, MrBayes shows a value called *average standard deviation of split sequences*. This value tells how distant are the cold chains of each run. The lower its value, the most similar are the trees sampled by both cold chains. This means that both runs are looking at the sample place in the tree space, so it is very probable that the real most probable tree is located around there. If the value is high, it means that each run is considering a different tree, so the analysis needs to run for more time or maybe there is some problem with our data or the model.

```
   Average standard deviation of split frequencies: 0.229602
```

It is considered that the analysis has finished when this value is lower than 0.01. If it does not reach this value after 100 million generations, it will never reach it, so we must stop the analysis and consider checking our dataset.

When MrBayes finishes the number of generations that we set, it will wask if we want to continue the analysis or not. Depending on the value of the standard deviation, we must choose `yes` and add more generations, or choose `no` and stop the analysis.

## Checking the analysis

After stopping the analysis, we must summarize the parameters using this simple command:

```
sump
```

This command summarizes the parameters of the analysis. It shows some information about them, but the interesting part is above. If we scroll a bit upwards, we will se a graph like this:

```
   +------------------------------------------------------------+ -4719.39
   |                                    2                       |
   |                                                           2|
   |2     222                           12      2               |
   |                              2                         2   |
   | 2 2           22           2                            12 |
   |  1 2      2               2 2    22 122  1     2           |
   |     2  1    2   *             1 *               2          |
   |         1         11 112* 1   2      1 *  2 2    2       1 |
   |       1 2*   *1  * 21    2  1           2     21    2 2    |
   | 1 1        11  1         1 1 1   1    1 12      1 *  1 1   |
   |1 2        1          221                     2   1 2  1   1|
   |     11     2      2            *  1        1       1       |
   |    1                2                        11      2  2  |
   |                                           1 1              |
   |                                                     1      |
   +------+-----+-----+-----+-----+-----+-----+-----+-----+-----+ -4735.46
   ^                                                            ^
   250000                                                       1000000
```

What is the meaning of this graph?

If we plot the probability/likelihood values (L) of the trees sampled in each generation, we should see something similar to this picture:

![Graph](media/Tmb-01-graph.png) 

First, it grows fast, and then it reaches a stationary phase. During the first generations, in which the probability is still growing, the sampled trees are still far from the optimal tree. Thus, we should remove this phase before processing our results to get our definitive tree; this is called **burn in**.

The MrBayes graph is equivalent to this representation, but:

- By default has removed the first 25% of generations (we can change this percentage), leaving only the stationary phase.
- This stationary phase is scaled, it is a horizontal line but extremely enlarged, so instead of a line it looks like a cloud of dots.

In the MrBayes graph, the numbers (1 and 2) correspond to the runs. Alternatively, it is marked with an asterisk if both runs had the same value for that generation.

A uniform cloud means that our analysis is good. But if the numbers form any kind of shape (diagonal line, curve, etc), that means that our analysis did not reach the stationary phase, and we must add more generations or check if there is any problem with our dataset. In the example above it looks a bit wavy because this example analysis is based on a very limited dataset. Ideally, the numbers should be distributed throughout all the graph area.

## Getting the tree

In order to get the consensus tree, we use the command “sumt”:

```
sumt
```

Just like `sump`, `sumt` applies a 25% burnin as default, but this value can be changed.

Our consensus tree will be stored as a file with the extension `.con.tre`, in NEXUS format.

Finally, we can close MrBayes using the command `quit`:

```
quit
```

















