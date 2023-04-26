# Gaps and missing data

One of the main controversies in phylogenetics is how the programs codify and analyze **gaps**, i.e. "jumps" in the sequence produced by **insertions** or **deletions**. When we align the sequences, a gap is generated in those sequences that do not have a corresponding nucleotide to those that are present in other sequences. They are usually represented by a dash `-`, for example:

```
              1    1    2    2    3
         5    0    5    0    5    0

Seq1 ATCGA----AGCTAGGTAGCTAGCGATCGA
Seq2 ATCGA----AGCTAGCTAGCTAGCGATCGA
Seq3 ACCGA----AGCTAGCTAGCT-GCGATAGA
Seq4 ATCGA--TGAGCTAGCTAGCT-GCGATCGA
Seq5 ATCGA--TGATCTAGCTAGCT-GCTATCGA
Seq6 ATCGATCTAGGCTAGCTAGCT-GAGATCGA
Seq7 ATCGATCTGAGCTAGACAGCT-GCGATCGA
```

Originally, they were analyzed considering them as a fifth nucleotide (protocol called **"gaps as 5th state"**), but some people critizized this methodology because the gaps do not actually exist: they are an abstract concept that we invented to be able to align the matrices.

An alternative vision is to interpret them as **missing data**, which is how we codify unknown nucleotides from bad quality or incomplete sequences (usually represented by an interrogation mark). This approach was also critizized, because both concepts are different and should be addressed in a different way.

A proposed solution suggested to remove these positions, and codify the gaps in the matrix as standard characters (zeros and ones, meaning absence or presence of a character). This is easy if our gaps are simple, such as the position 22 of the matrix above: it is clear that the gap is present in some sequences and absent from anothers. But what happens with the gap(s) in positions 6 to 9? Is the big gap in the sequences 1 to 3 homologous (has the same origin) to the smaller gap in sequences 4 and 5? Does it derive from it or has an independent origin? Or do we have two different gaps, one in positions 6 and 7, and another in positions 8 and 9?

Another strategy, equivalent to sweeping the dirt under the carpet, is to remove any position with gaps from our analysis. But this can remove essential information for resolving our phylogeny. **Be aware that most programs silently use this approach!**

The debate still continues while the theoreticians look for a definitive solution for this uncomfortable problem.
