#! /usr/bin/env python

a = "sequence.nucleotide.gb"
with open(a, "r") as handle:
    title = ""
    seq_list = []
    origin_start = False
    for line in handle.readlines():
        line = line.strip()
        if line.startswith("  TITLE     "):
            origin_start = True
            seq_list.append(line[12:])
        elif origin_start == True and line[0:12] == " " * 12:
            seq_list.append(line[12:])
        elif line.startswith("JOURNAL"):
            origin_start = False
        else:
            pass

print("  TITLE     " + ("\n" + " " * 12).join(seq_list))
