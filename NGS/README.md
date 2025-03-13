# NGS for dummies

This is a tutorial for the pipeline that we follow for NGS data in our lab. 

## Wet lab

### Basics

Illumina is a high-throughput sequencing by synthesis. What does this mean?

-	**High-throughput**: it’s going to sequence a lot of DNA fragments at once.
-	**By synthesis**: the machine will determine which nucleotide is at a particular position by synthetizing the complementary chain, and detecting the light emitted by the new nucleotide when it is inserted.

Yes, we are going to sequence **all our samples** (specifically, their COI fragments) in a single batch.

Here it is explained how our primers with tags work and their structure:

- [Primers and tags](/Primers.md).

Here we give an example of how to design our plates and organize the primer combinations:

- [Plate design for the Sonata project](/Plates.md).

### PCR

For the PCR we take our plate, and in each well, we add:

- 2 uL of the **DNA extraction**.
- 2.25 uL of each **primer** (4.5 uL in total).
- 7.5 uL of the Qiagen polymerase **master mix**.
- 1 uL of **water**.

(I usually combine the master mix and the water for all the samples in a single tube, and then dispense 8.5 uL of that mix in each well).

The PCR program is:

- 95ºC for 15:00
- 35 steps of
	- 94ºC for 0:30
	- 50ºC for 1:30
	- 72ºC for 1:30
- 72ºC for 10:00

### Equimolar pooling

After running the PCR, we need to mix all the PCR products in a single pool, but including the same amount of DNA from each of them. In order to do this, we need to know the DNA concentration in each PCR product. We take the measurements using a Qubit, and then calculate how much volume of each PCR product we need to take to get 100ng of DNA (just divide 100 by your concentration in ng/uL).

### Sequencing

When all the PCR products of our plates have been mixed in a single pool, it's ready to be sent to the sequencing service for its transformation into an Illumina library and sequencing. Here are some details about the sequencing process and the output:

- [Sequencing](/Sequencing.md).

## Bioinformatics

### Pre-requirements

- If you are using a Windows computer, install the Windows subsystem for Linux ([Instructions](/WSL.md)).

- Install the [pre-required packages](/Prerequirements.md).


