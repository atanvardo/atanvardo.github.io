# Sequencing

Currently, we are using one Illumina MiSeq v2 kit that produces 20 million sequences (in the UJ, we have to buy the kit ourselves and send it with the pools to Wiesiek's lab). One kit is enough to sequence 8 libraries (8 pools of 4 plates, or 2944 samples). If the number of samples is smaller, we can use the smaller kit that gets 1 million sequences.

Some sequencing services require that we run our pools in an agarose gel and isolate the band that correspond to our target marker, as there are usually other bands corresponding to inspecific amplification or primer dimers that may "stain" our libraries.

The sequencing service can ask if we want to include something called PhiX control. The answer is usually yes. It is a bunch of random sequences from the PhiX phage that are included to give more heterogeneity to the DNA in the flow cell. If our sequences are similar, as in our case (because they are all the same marker), it is possible that most of them have the same nucleotide in a particular position. In the absence of the PhiX control, this will create a huge monochromatic flash in each sequencing step that will hide different nucleotides in a minority of sequences. For example, imagine that most of the sequences have a T in the position that is being read, and some have a C. The flash of the T color will be so bright that the sequencer will not be able to see the flash of the C nucleotides, and will incorrectly assign a T to all the sequences. The PhiX control, being basically random nucleotides, adds color diversity and solves this problem. Then, the Illumina sequencer automatically removes the PhiX sequences from the result.

Each sequence is read from the two extremes, creating two reads (R1 and R2) that will be combined during the bioinformatic process.

# The sequencing output

The Illumina machine created two FASTQ files, for example:

```
tardi-pilot_S1_L001_R1_001.fastq
tardi-pilot_S1_L001_R2_001.fastq
```

Each file corresponds to one of the reads (R1 and R2). Logically, both of them had the same size and the same number of sequences.

A FASTQ file stores each sequence in four lines:


```
@M01530:85:000000000-DCVCM:1:1101:17604:28769 1:N:0:1
AAACCGACCCGATATGGCTTTCCCA…
+
CBCCCCCCCCCCGGGGGGGGGGHHH…
```

The first line is the name of the sequence. It includes a series of data separated by colons (:). From left to right, we have:

-	The ID of the sequencer, in this case M01530.
-	The run number in that sequencer. In this case, it means that our sequencing reaction was the 85th made in that sequencer.
-	The serial number of the flow cell, in this case 000000000-DCVCM.
-	The lane of that flow cell. Our flow cell only had one lane, so this value could only be 1.
-	The tile within that lane where this DNA fragment was located, in this case 1101.
-	The two following numbers (17604 and 28769) are the physical coordinates of the flow cell where this DNA fragment was located.
-	The read number, in this case 1 because this sequence comes from the R1 file.
-	A letter indicated if this read has been filtered by the sequencer, in this case it’s an N which means no.
-	A number that indicates if the sequence is from a control, in this case 0 which means no.
-	Finally, the read index, not used in this case.

The second line is the sequence.

The third line is a + sing.

The fourth line is the quality of the sequence, codified in ASCII characters. 
