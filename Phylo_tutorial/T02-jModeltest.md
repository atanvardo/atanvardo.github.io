# Tutorial 2: Model testing with jModelTest

jModelTest allow us to test which is the most appropriate nucleotide substitution model for our dataset. This is very important, as using a suboptimal model may produce incorrect results. In theory, using the most complex model (GTR+I+G) will give the most reliable phylogenies, but not always. Additionally, the GTR model requires more computing power that simpler models, and a most suitable and less complex model will help our analysis to finish sooner.

This program carries a Maximum Likelihood analysis with each model. At the end, it compares the likelihood values, corrected according to the number of parameters of each model, and determines which is the most optimal.

## Installing jModelTest

jModelTest can be downloaded from [its GitHub](https://github.com/ddarriba/jmodeltest2) repository. On the right panel we can find the link to the latest release, and download it from the Full Release link.

It will create a `.tar.gz` file in our computer, that we can unzip (for example, using 7zip).

Inside, we will find the jModelTest executable as a `jar` file (we will need to have a Java framework, such as OpenJDK, installed in our system).

## Loading the data

When we execute jModelTest, it will show a ugly window. In order to load our input file (preferably in NEXUS format) we select `File` > `Load DNA alignment`, find our file, and load it.

If everything is fine, jModelTest will show a couple of lines indicating how many sequences are in our alignment and their length. In case of error, it will give some information about what happened so you can correct your data file.

## Comparing models

To compare the models, we select `Analysis` > `Compute Likelihood scores`, and this window will pop up:

![Comparing](media/Tjmodeltest-01-comparing.png)

We should be ***extremely careful*** when selecting the parameters in the `Likelihood settings` section.

The default parameters will compare a total 88 models, as it will test:

-	11 nucleotide substitution schemes.
-	Including, or not, different frequencies for each nucleotide (**+F**).
-	Including, or not, the proportion of invariant sites (**+I**).
-	Including, or not, the shape of the gamma distribution (**+G**).

In total: 11 x 2 x 2 x 2 = 88.

But, is our phylogenetic program able to deal with all these parameters?

For example, MrBayes and BEAST only admit three different nucleotide substitution schemes (JC, HKY and GTR), so testing additional models is a waste of time. If we are going to use these programs, we should select `3` in the `Number of substitution schemes` option, and jModelTest will only compare these models (24 combinations in total, including the optional parameters).

The analysis will start when we click on `Compute Likelihoods`. The speed of the analysis depends on how many processors we allowed it to use.

When it finishes, we must click on `Analysis` > `Do AIC calculations`. In the options, we should leave the default parameters, unless our matrix is very small. If everything is fine, we click on `Do AIC calculations` and jModelTest will run this additional analysis.

## Interpreting the results

In order to see how each model compares to the others, we should scroll upwards in the output screen, until we find a table similar to this one:

![Output](media/Tjmodeltest-02-output.png)

This table sort the models, starting from the most fitting to the less appropriate. In this case, the best model is GTR+I+G.

In order to correctly interpret the results and translate them to our phylogenetic software, we must keep in mind the **![table of nucleotide substitution models](https://github.com/atanvardo/Phylo-Tutorial/blob/main/04-Nucleotide%20substitution%20models.md#table-of-nucleotide-substitution-models)**.

**Warning**: Not every program uses the same nomenclature for the nucleotide substitution models, but if we know how many rates of substitution we should include and what are the extra parameters, we can know how to read the jModelTest table and translate it to any program. For example, looking at the table, we can see that the model `F81` is equivalent to the model `JC` including different nucleotide frequencies, so if some program calls a model `F81` and another program says `JC+F`, they are the same model.
