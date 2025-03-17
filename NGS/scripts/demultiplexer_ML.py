## Script by Alejandro Lopez-Lopez
## version of 19/08/2024
## Aims of the script: We received sequences from an Illumina run
## in which the tags (and in some cases the primers) are incomplete.
## This prevents us to use other scripts in published pipelines, so
## we had to create this script. This script will read the sequences,
## select those that are identifiable by the tag, and them demultiplex
## them, saving them in different files corresponding to the different
## samples. We will also remove the tags and primers and leave them
## ready to be # processed.
##
## -----------------------------------------------------------------------
## INPUT
## -----------------------------------------------------------------------
## We need the following input files:
## - The two reads file (R1 and R2) in FASTQ format.
## - A file listing the primers.
## - A file listing the tags.
## - A file listing our samples and the corresponding primers and tags.
## The format of the files is detailed below:
##
## ------------------------------------------------------------------------
## Primers file
## -----------------------------------------------------------------------
## Tabulated text file with three columns:
## a) Name of the marker
## b) Direction of the primer (F or R)
## c) Sequence of the primer
## For example:
## DEP5	F	CCGTAATCDATNGAYTTYTG
## DEP5	R	GAAARRTAYGANGAYTGG
## EIF	F	CCGCCARTGYTTHTCSAC
## EIF	R	TGGYCARGARRTBGARGT
##
## ------------------------------------------------------------------------
## Tags file
## -----------------------------------------------------------------------
## Tabulated text file with two columns:
## a) Number of the tag
## b) Sequence of the tag
## For example:
## 1	AACCGA
## 2	CCGGAA
## 3	AGTGTT
## 4	CCGCTG
##
## ------------------------------------------------------------------------
## Samples file
## -----------------------------------------------------------------------
## Tabulated text file with four columns:
## a) Marker
## b) Tag of the forward primer
## c) Tag of the reverse primer
## d) Name of the sample
## For example:
## COI	1	1	MP1
## COI	1	2	MP2
## COI	1	3	MP3
## COI	1	4	MP4
##
## -----------------------------------------------------------------------
## INSTRUCTIONS
## -----------------------------------------------------------------------
## - Change the names of the files and the project in the following lines.
## - Change the name of the project (the script will save the output files
##   in a folder with that name).
## - Run the script (python demultiplexer_ML.py).
##
## -----------------------------------------------------------------------

import os

name_of_the_primers_file = "_primers.txt"
name_of_the_tags_file = "_tags.txt"
name_of_the_samples_file = "_samples_payal.txt"
name_of_the_R1_sequences_file = "18S_S4_L001_R1_001.fastq"
name_of_the_R2_sequences_file = "18S_S4_L001_R2_001.fastq"
project_name = "Payal"


class Primer:

    def __init__(self, marker, direction, sequence):
        self.marker = marker
        self.direction = direction
        self.sequence = sequence


class Tag:

    def __init__(self, number, sequence):
        self.number = number
        self.sequence = sequence


class Sequence:

    def __init__(self, name, marker, direction, tagcode, sequence, qc):
        self.name = name
        self.marker = marker
        self.direction = direction
        self.tagcode = tagcode
        self.sequence = sequence
        self.qc = qc


# Definition of functions that will be used in the script:

def identifier(sequencelines, primerlist, taglist, tolerance):
    # This function checks in a sequence has any of the primers of the provided list in the possible positions (0 to 7).
    # It will retirn a Sequence object.

    # The input will be a list of the four text lines that store the information about the sequence in the FASTQ file.
    # First, we isolate the name of the sequence (the first line), the sequence (secound line), and the quality
    # (third line).
    sequence_name = sequencelines[0].strip()
    sequence = sequencelines[1].strip()
    sequence_qc = sequencelines[3].strip()

    # If we find the primer, we will trim the sequence. For now, we'll store the complete sequence here (just in
    # case we don't find any primer).
    trimmed_sequence = sequencelines[1].strip()
    trimmed_qc = sequencelines[3].strip()

    # We set the values for the marker, direction and the tag as "Unknown" by default. These values will be changed
    # if we find the primer
    marker = 'Unknown'
    direction = 'Unknown'
    tagcode = 'Unknown'

    # We create a dictionary of the equivalences of the possible ambiguities in the primers
    char2nuc = {'A': ['A'],
                'T': ['T'],
                'C': ['C'],
                'G': ['G'],
                'R': ['A', 'G'],
                'Y': ['C', 'T'],
                'N': ['A', 'C', 'G', 'T'],
                'W': ['A', 'T'],
                'S': ['G', 'C'],
                'M': ['A', 'C'],
                'K': ['G', 'T'],
                'B': ['C', 'G', 'T'],
                'H': ['A', 'C', 'T'],
                'D': ['A', 'G', 'T'],
                'V': ['A', 'C', 'G']}

    # And now, we start to look for the primer.
    # We start from the first position, and move to the eigth. As we have a possible extra nucleotide, six
    # nucleotides corresponding to the tag (some of them may be missing, but we'll take care of that later,
    # and then the primer, the primer should not start further away.
    for position in range(0, 8):
        # In each position, we check if the sequence that starts there correspond to any of the primers.
        for primer_to_evaluate in primerlist:
            target = sequence[position:(position + len(primer_to_evaluate.sequence))]
            difs = 0
            for nuc in range(len(target)):
                # For each nucleotide in our target sequence, if it does not correspond to the nucleotide in
                # the primer, we will add one difference
                if target[nuc] not in char2nuc[primer_to_evaluate.sequence[nuc]]:
                    difs += 1
            if difs <= tolerance:
                # If the number of differences is less than our tolerance (we include some margin of error
                # to account for possible sequencing errors, 3 differences by default), the primer is at that position!
                marker = primer_to_evaluate.marker
                direction = primer_to_evaluate.direction

                # Now we deal with the tag. It will correspond to the nucleotides before the primer.
                tag_sequence = sequence[0: position]
                if len(tag_sequence) == 0:
                    # If the tag is missing, it will be unknown.
                    tagcode = 'Unknown'
                if len(tag_sequence) > 6:
                    # If the tag is longer than 6 nucleotides, it means that we have some extra base(s) before. We
                    # remove them.
                    tag_sequence = tag_sequence[-6:]
                for tag in taglist:
                    if tag.sequence == tag_sequence:
                        tagcode = tag.number

                # Now we get the trimmed sequences, without the primer and the tag. We don't need the tag anymore.
                # And the primers, being degenerated, have been sequenced with some variation, leaving them will
                # cause problems during the assembling of the sequences.
                # (Notice that the sequences where no primer is found will be saved complete, as that is the
                # default value).
                trimmed_sequence = sequence[position:]
                trimmed_qc = sequence_qc[position:]

    return Sequence(sequence_name, marker, direction, tagcode, trimmed_sequence, trimmed_qc)


def savelines(folder, prefix, r1lines, r2lines):
    # This function saves the lines to the prefix_R1.fastq and prefix_R2.fastq files
    r1filename = folder + '/' + prefix + '_R1.fastq'
    r2filename = folder + '/' + prefix + '_R2.fastq'
    # If the folder doesn't exist, create it:
    if not os.path.exists(folder + '/'):
        os.makedirs(folder)
    if os.path.exists(r2filename):
        # The files have been created, so we append the lines
        r1file = open(r1filename, 'a')
        r2file = open(r2filename, 'a')
        for line in r1lines:
            r1file.write(line)
        for line in r2lines:
            r2file.write(line)
        r1file.close()
        r2file.close()
    else:
        # These are the first sequences to be stored in that file, so we have to create it
        r1file = open(r1filename, 'w')
        r2file = open(r2filename, 'w')
        for line in r1lines:
            r1file.write(line)
        for line in r2lines:
            r2file.write(line)
        r1file.close()
        r2file.close()
    return 0


def classify(projectname, r1filename, r2filename, samplecombinations, sampledictionary):
    # This is the main function of the script. It will read the two fasta files, taking 4 lines (1 fastq sequence)
    # each time. Every group of four lines includes:
    #   Line 1: name of the sequence, preceded by "@"
    #   Line 2: the sequence
    #   Line 3: the symbol "+"
    #   Line 4: the quality score of the sequence
    # For each group of four lines, it will call the "identifier" function to get which marker, direction and
    # tag it has. Then:
    # If the tags are Unknown: it will store the sequences in the Unknown_R1 and Unknown_R2 files.
    # Else:
    #   If the marker is different, it will store the sequences in the sample_MismatchM files.
    #   If the marker is the same, it will check if the directions are different.
    #       If the directions are the same, it will store the sequences in the sample_MismatchD files.
    #       If the directions are different, it will store the sequences in the sample_marker files.

    # We start initializing the files:
    r1file = open(r1filename, 'r')
    r2file = open(r2filename, 'r')

    # And now we start reading the lines of the r1file and r2file by groups of four.
    # We will store the groups of four lines in these lists:
    logfile = open('log.txt', 'a')
    sequence_lines_r1 = []
    sequence_lines_r2 = []
    for line_r1, line_r2 in zip(r1file, r2file):
        # We read one line of each file and add it to the list
        sequence_lines_r1.append(line_r1)
        sequence_lines_r2.append(line_r2)
        # If after this we have four items in each list, that means that we have the four lines
        # that define each sequence, and we can process them.
        if len(sequence_lines_r1) == 4:
            # First, we identify the marker, direction, and tags of the sequences:
            identity_r1 = identifier(sequence_lines_r1, primers, tags, 3)
            identity_r2 = identifier(sequence_lines_r2, primers, tags, 3)
            # We check if at least one of the tags in Unknown, and in that case we store the sequences
            # in the file corresponding to the unknown tags:
            if 'Unknown' in [identity_r1.tagcode, identity_r2.tagcode]:
                savelines(projectname, 'Unknowntag', sequence_lines_r1, sequence_lines_r2)
            # If not, we check if both markers don't match:
            elif identity_r1.marker != identity_r2.marker:
                savelines(projectname, 'MismatchM', sequence_lines_r1, sequence_lines_r2)
            # If both markers are the same, the directions must be different. If not, we discard them
            elif identity_r1.direction == identity_r2.direction:
                savelines(projectname, 'MismatchD', sequence_lines_r1, sequence_lines_r2)
            # If all the previous checks are false, then we have a good pair of sequences
            else:
                # First, we identify which is the R1 tag and the R2 tag.
                if identity_r1.direction == 'F':
                    tag1 = identity_r1.tagcode
                    tag2 = identity_r2.tagcode
                else:
                    tag1 = identity_r2.tagcode
                    tag2 = identity_r1.tagcode
                # Now we get the combination of marker and tags to get the sample name
                mtt = identity_r1.marker + '_' + tag1 + '_' + tag2
                if not mtt in samplecombinations:
                    # In this case we have a unknown sample
                    savelines(projectname, 'Unknown_' + identity_r1.marker, sequence_lines_r1, sequence_lines_r2)
                else:
                    # As we will include the trimmed sequences, we need to create a new set of lines for
                    # our file
                    lines_r1 = []
                    lines_r2 = []
                    lines_r1.append(identity_r1.name + '\n')
                    lines_r2.append(identity_r2.name + '\n')
                    lines_r1.append(identity_r1.sequence + '\n')
                    lines_r2.append(identity_r2.sequence + '\n')
                    lines_r1.append('+\n')
                    lines_r2.append('+\n')
                    lines_r1.append(identity_r1.qc + '\n')
                    lines_r2.append(identity_r2.qc + '\n')
                    # We get the name of our sample
                    sample = sampledictionary[mtt]
                    # And now we save them
                    savelines(projectname, sample + '_' + identity_r1.marker, lines_r1, lines_r2)
            # And, after processing these lines, we reset the list to leave them clean, waiting to read
            # the next sequence:
            sequence_lines_r1 = []
            sequence_lines_r2 = []

    logfile.close()


# We read the tags table and store that information in a dictionary for the identification of samples
tagfile = open(name_of_the_tags_file)
tags = []
for line in tagfile:
    l = line.strip().split('\t')
    tag = Tag(l[0], l[1])
    tags.append(tag)
tagfile.close()


# We read the primer info and store that information in a dictionary for the identification of samples
primerfile = open(name_of_the_primers_file)
primers = []
for line in primerfile:
    l = line.strip().split('\t')
    primer = Primer(l[0], l[1], l[2])
    primers.append(primer)
primerfile.close()


# We read the table with the samples
# COI	1	1	MP1
samplefile = open(name_of_the_samples_file)
marker_tag1_tag2_combinations = []
marker_tag1_tag2_2_samplename = {}
for line in samplefile:
    l = line.strip().split('\t')
    marker = l[0]
    tag1 = l[1]
    tag2 = l[2]
    samplename = l[3]
    mtt = marker + '_' + tag1 + '_' + tag2
    marker_tag1_tag2_combinations.append(mtt)
    marker_tag1_tag2_2_samplename[mtt] = samplename


classify(project_name, name_of_the_R1_sequences_file, name_of_the_R2_sequences_file, marker_tag1_tag2_combinations, marker_tag1_tag2_2_samplename)

print('Done!')
