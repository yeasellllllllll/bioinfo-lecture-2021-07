#! /usr/bin/env python

# Op1) Read a FASTA format DNA sequence file
#     and make a reverse sequence file.
# Op2) Read a FASTA format DNA sequence file
#      and make a reverse complement sequence file.
# Op3) Convert GenBank format file to FASTA format file.

a = "sequence.nucleotide.fasta"
# Op1) Read a FASTA format DNA sequence file
#     and make a reverse sequence file.
with open(a, "r") as handle1:
    title = ""
    seq_list = []
    for line in handle1.readlines():
        line = line.strip()
        if line == "":
            continue
        elif line.startswith(">") != True:
            seq_list.append(line)
        else:
            title = line

seq = "".join(seq_list)
r_seq = seq[::-1]
rr_seq = f"{title}\n {r_seq}"

with open("r_sequence.nucleotide.fasta", "w") as handle2:
    handle2.write(rr_seq)
# Op2) Read a FASTA format DNA sequence file
#      and make a reverse complement sequence file.
with open("r_sequence.nucleotide.fasta", "r") as handle3:
    title = ""
    seq_list = []
    cseq_list = []
    d_seq = {"A": "T", "T": "A", "G": "C", "C": "G"}
    for line in handle3.readlines():
        line = line.strip()
        if line == "":
            continue
        elif line.startswith(">") != True:
            seq_list.append(line)
        else:
            title = line

seq = "".join(seq_list)
for i in seq:
    cseq_list.append(d_seq[i])
rc_seq = "".join(cseq_list)
rrc_seq = f"{title}\n {rc_seq}"

with open("rc_sequence.nucleotide.fasta", "w") as handle4:
    handle4.write(rrc_seq)

# Op3) Convert GenBank format file to FASTA format file.
b = "sequence.nucleotide.gb"

with open(b, "r") as handle5:
    lines = handle5.readlines()

with open("new.sequence.nucleotide.fasta", "w") as handle6:
    for line in lines:
        handle6.write(line)
