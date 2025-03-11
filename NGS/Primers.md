# Primers and tags

We are going to group all our samples in a single library for sequencing.

But, how will we separate the sequences corresponding to each sample? Easy. First, we will amplify our marker from each sample by a normal PCR, but using different variants of the primers. For each sample, both the forward and the reverse primers will have a “**tag**”, i.e. six additional nucleotides that will be sequenced and will determine which sample each sequence corresponds to.

For example, the primers that we are using to amplify the COI for the Sonata project are the following:

| COIBF3 | Forward | `CCHGAYATRGCHTTYCCHCG` |
| COIBR2 | Reverse | `TCDGGRTGNCCRAARAAYCA` |

And we are using a total of 24 tags:

| 1 | `AACCGA` | 9 | `GAACTA` | 17 | `CTAGGC` |
| 2 | `CCGGAA` | 10 | `CACAGT` | 18 | `TGAGGT` |
| 3 | `AGTGTT` | 11 | `CAATCG` | 19 | `TCAACT` |
| 4 | `CCGCTG` | 12 | `CCGTCC` | 20 | `TACACA` |
| 5 | `AACGCG` | 13 | `GGGACA` | 21 | `GATGAC` |
| 6 | `GGCTAC` | 14 | `AGCTCA` | 22 | `AGTAGA` |
| 7 | `TTCTCG` | 15 | `ACTGGG` | 23 | `TCCTTT` |
| 8 | `TCACTC` | 16 | `GATCGG` | 24 | `ATGAGG` |

These tags have been selected to have a Hamming distance (nucleotide differences) greater than 3, to avoid that one tag changes to another by a PCR or sequencing error.

Adding these tags to each primer create 24 different variants for each primer.

For example, the sequence of the 8th variant of the primer COIBF3 (we will call it COIBF3_8) is `NTCACTCCCHGAYATRGCHTTYCCHCG`, which is composed of:

- A random nucleotide `N` at the beginning, included following the recommendations by Wiesiek Babik.
- The tag number 8 (`TCACTC`).
- The primer COIBF3 (`CCHGAYATRGCHTTYCCHCG`)
