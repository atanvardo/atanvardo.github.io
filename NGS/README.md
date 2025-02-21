# NGS for dummies

This is a tutorial for the pipeline that we follow for NGS data in our lab. 

## Wet lab

### Basics

Illumina is a high-throughput sequencing by synthesis. What does this mean?

-	**High-throughput**: it’s going to sequence a lot of DNA fragments at once.
-	**By synthesis**: the machine will determine which nucleotide is at a particular position by synthetizing the complementary chain, and detecting the light emitted by the new nucleotide when it is inserted.

Yes, we are going to sequence **all our samples** (specifically, their COI fragments) in a single batch.

### Primers and tags

But, how did we separate the sequences corresponding to each sample? Easy. First, we amplified the COI of each sample by a normal PCR, but in which the primers contained a “**tag**”, i.e. six additional nucleotides that will be sequenced and will determine which sample each sequence corresponds to.

The primers (for the COI) are the following:

| COIBF3_x | Forward | `NxxxxxxCCHGAYATRGCHTTYCCHCG` |
| COIBR2_x | Reverse | `NxxxxxxTCDGGRTGNCCRAARAAYCA` |

For the Sonata project we use a total of 24 tags:

| 1 | AACCGA | 9 | GAACTA | 17 | CTAGGC |
| 2 | CCGGAA | 10 | CACAGT | 18 | TGAGGT |
| 3 | AGTGTT | 11 | CAATCG | 19 | TCAACT |
| 4 | CCGCTG | 12 | CCGTCC | 20 | TACACA |
| 5 | AACGCG | 13 | GGGACA | 21 | GATGAC |
| 6 | GGCTAC | 14 | AGCTCA | 22 | AGTAGA |
| 7 | TTCTCG | 15 | ACTGGG | 23 | TCCTTT |
| 8 | TCACTC | 16 | GATCGG | 24 | ATGAGG |

For example, the sequence of the primer COIBF3_8 is `NTCACTCCCHGAYATRGCHTTYCCHCG`.

These tags have been selected to have a Hamming distance (nucleotide differences) greater than 3, to avoid that one tag changes to another by a PCR or sequencing error.

The `N` at the beginning of each primer sequence is a random nucleotide that was included following the recommendations by Wiesiek Babik.

### Plate design for the Sonata project

These 24 tags are enough to amplify 576 samples (6 plates). But, during the design of the experiment, we decided that each batch would be composed only by 384 samples (4 plates), by using a combination of 16 forward primers and 24 reverse primers. In each row we will add one of the variants of the F primer, and in each column a variant of the R primers:

| **Plate 1** | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 |
| F1 |  |  |  |  |  |  |  |  |  |  |  |  |
| F2 |  |  |  |  |  |  |  |  |  |  |  |  |
| F3 |  |  |  |  |  |  |  |  |  |  |  |  |
| F4 |  |  |  |  |  |  |  |  |  |  |  |  |
| F5 |  |  |  |  |  |  |  |  |  |  |  |  |
| F6 |  |  |  |  |  |  |  |  |  |  |  |  |
| F7 |  |  |  |  |  |  |  |  |  |  |  |  |
| F8 |  |  |  |  |  |  |  |  |  |  |  |  |

<br>

| **Plate 2** | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 |
| F1 |  |  |  |  |  |  |  |  |  |  |  |  |
| F2 |  |  |  |  |  |  |  |  |  |  |  |  |
| F3 |  |  |  |  |  |  |  |  |  |  |  |  |
| F4 |  |  |  |  |  |  |  |  |  |  |  |  |
| F5 |  |  |  |  |  |  |  |  |  |  |  |  |
| F6 |  |  |  |  |  |  |  |  |  |  |  |  |
| F7 |  |  |  |  |  |  |  |  |  |  |  |  |
| F8 |  |  |  |  |  |  |  |  |  |  |  |  |

<br>

| **Plate 3** | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 |
| F9 |  |  |  |  |  |  |  |  |  |  |  |  |
| F10 |  |  |  |  |  |  |  |  |  |  |  |  |
| F11 |  |  |  |  |  |  |  |  |  |  |  |  |
| F12 |  |  |  |  |  |  |  |  |  |  |  |  |
| F13 |  |  |  |  |  |  |  |  |  |  |  |  |
| F14 |  |  |  |  |  |  |  |  |  |  |  |  |
| F15 |  |  |  |  |  |  |  |  |  |  |  |  |
| F16 |  |  |  |  |  |  |  |  |  |  |  |  |

<br>

| **Plate 4** | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 |
| F9 |  |  |  |  |  |  |  |  |  |  |  |  |
| F10 |  |  |  |  |  |  |  |  |  |  |  |  |
| F11 |  |  |  |  |  |  |  |  |  |  |  |  |
| F12 |  |  |  |  |  |  |  |  |  |  |  |  |
| F13 |  |  |  |  |  |  |  |  |  |  |  |  |
| F14 |  |  |  |  |  |  |  |  |  |  |  |  |
| F15 |  |  |  |  |  |  |  |  |  |  |  |  |
| F16 |  |  |  |  |  |  |  |  |  |  |  |  |

For example, the sample in the F2 well of the first (upper left) plate was amplified using the primers COIBF3_6 and COIBR2_2. The sample in the E4 well of the fourth (lower right) plate will be amplified using the primers COIBF3_13 and COIBR2_16.

In each plate, the total number of samples is actually 92. We randomly choose two wells to leave them blank as negative controls (to detect contamination), and we choose two samples to be duplicated as a sequencing control (we expect to get the same sequence for each pair of duplicates at the end).

### PCR

In each well, we will add:

- 2 uL of the DNA extraction.
- 2.25 uL of each primer (4.5 uL in total).
- 7.5 uL of the Qiagen polymerase master mix.
- 1 uL of water.

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

When all the PCR products of our plates have been mixed in a single pool, it's ready to be sent to the sequencing service for its transformation into an Illumina library and sequencing.

Currently, we are using one Illumina MiSeq v2 kit that produces 20 million sequences (in the UJ, we have to buy the kit ourselves and send it with the pools to Wiesiek's lab). One kit is enough to sequence 8 libraries (8 pools of 4 plates, or 2944 samples). If the number of samples is smaller, we can use the smaller kit that gets 1 million sequences.

Some sequencing services require that we run our pools in an agarose gel and isolate the band that correspond to our target marker, as there are usually other bands corresponding to inspecific amplification that may "stain" our libraries.

The sequencing service can ask if we want to include something called PhiX control. The answer is usually yes. It is a bunch of random sequences from the PhiX phage that are included to give more heterogeneity to the DNA in the flow cell. If our sequences are similar, as in our case (because they are all the same marker), it is possible that most of them have the same nucleotide in a particular position. In the absence of the PhiX control, this will create a huge monochromatic flash in each sequencing step that will hide different nucleotides in a minority of sequences. For example, imagine that most of the sequences have a T in the position that is being read, and some have a C. The flash of the T color will be so bright that the sequencer will not be able to see the flash of the C nucleotides, and will incorrectly assign a T to all the sequences. The PhiX control, being basically random nucleotides, adds color diversity and solves this problem. Then, the Illumina sequencer automatically removes the PhiX sequences from the result.

Each sequence is read from the two extremes, creating two reads (R1 and R2) that will be combined during the bioinformatic process.

## Bioinformatics

