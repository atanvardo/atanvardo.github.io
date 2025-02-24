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

### The sequencing output

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

## Bioinformatics

### Windows Subsystem for Linux (WSL)

*If you have Linux installed in your computer, ignore this section*

The processing of the samples is preferably carried out in a Linux environment. A good solution for Windows users is to use the Windows Subsystem for Linux (WSL), which allows you to install and run a Linux distribution within Windows.

An easy way to get it is to access the Microsoft Store available in all the modern versions of Windows, and install the app Ubuntu, which installs this Linux distribution in your system.

When you load this app, it will start a Linux shell in your Linux home directory. WSL stores the Linux file system in this very hidden folder: `C:\Users\[your_user_name]\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs`

You should automatically have a bookmark to this folder available in the navigation pane of the Windows file explorer.

### Moving files between the WSL and Windows

This is VERY IMPORTANT. If you use Windows to copy a file from your Windows system to a folder in your Linux system, that file won’t have the required permissions to be used in Linux.

To move files from Windows to Linux, use the Linux command line. You copy (command `cp`) the file (to access the Windows file system from Linux, you have to go to the folder `/mnt/c`, which is equivalent to the `C:` drive) to the destination. For example, to copy the file `file.txt` that is in the Desktop of my Windows system to the folder `project` in my Linux home directory, I have to write in the Linux shell:

```
cp /mnt/c/Users/[windows_user_name]/Desktop/file.txt ~/project/
```

To copy from Linux to Windows, do it the opposite way:

```
cp file.txt /mnt/c/Users/[windows_user_name]/Desktop/
```

WARNING: Try to avoid deleting or moving files from the Linux system using the Windows file explorer! The Linux system will still believe that the files are there, and this can cause problems.

### Pre-required packages

In order to process our sequences, we will need to have some programs installed in our Linux system.

We are going to need the FASTX toolkit. You can install it following these commands:

```
cd /usr/local/src/

sudo wget https://github.com/agordon/libgtextutils/releases/download/0.7/libgtextutils-0.7.tar.gz

sudo tar -xzf libgtextutils-0.7.tar.gz

cd libgtextutils-0.7

sudo sed -i '47s/input_stream/static_cast<bool>(input_stream)/' src/gtextutils/text_line_reader.cpp

sudo ./configure

sudo make

sudo make install

cd ../

sudo wget https://github.com/agordon/fastx_toolkit/releases/download/0.0.14/fastx_toolkit-0.0.14.tar.bz2

sudo tar -xjf fastx_toolkit-0.0.14.tar.bz2

cd fastx_toolkit-0.0.14

sudo wget https://github.com/agordon/fastx_toolkit/files/1182724/fastx-toolkit-gcc7-patch.txt

sudo patch -p1 < fastx-toolkit-gcc7-patch.txt

sudo ./configure

sudo make

sudo make install

cd ../
```

We will also need PEAR. You need to “purchase” it (it’s free for users in academia!) here:

`https://www.h-its.org/downloads/pear-academic/`

They will send you a download link. Then you need to place the downloaded file in your Linux system, and run these commands, but **remember to modify them** to use the real folder where you place your PEAR installation file and the actual version that you downloaded:

```
cd /usr/local/src/

sudo cp ~/pear-0.9.11-linux-x86_64.tar.gz ./

sudo tar -xzf pear-0.9.11-linux-x86_64.tar.gz

cd pear-0.9.11-linux-x86_64

sudo cp bin/pear /usr/local/bin/

sudo gzip man/pear.1

sudo cp man/pear.1.gz /usr/share/man/man1/
```

Another software that we will need is BLAST and its associated programs. We can install it running the following commands, replacing [BLAST_VERSION] for the numbers of the last version of the software (you can check which ones are available going to `ftp.ncbi.nlm.nih.gov/blast/executables/blast+/` in your Internet browser.

```
cd /usr/local/src/

sudo wget "ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/[BLAST_VERSION]/ncbi-blast-[BLAST_VERSION]+-x64-linux.tar.gz"

sudo tar -zxf ncbi-blast-[BLAST_VERSION]+-x64-linux.tar.gz

sudo cp ncbi-blast-[BLAST_VERSION]+/bin/* /usr/local/bin/
```

And finally we will install FASTQC, which is straightforward:

```
cd /usr/local/src/

sudo wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip

sudo unzip fastqc_v0.11.9.zip

sudo chmod a+x FastQC/fastqc

sudo ln -s /usr/local/src/FastQC/fastqc /usr/local/bin/fastqc
```

We will also need to be sure that we have Python 3 installed in our Linux system.

```
sudo apt-get install python3
```

And we have to install CROP, which needs to be compiled from the source:

```
cd /usr/local/src

sudo git clone https://github.com/tingchenlab/CROP

sudo make
```

