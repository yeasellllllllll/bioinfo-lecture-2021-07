#! /usr/bin/env python

f = "sequence.protein.2.fasta"

with open(f, "r") as handle:
    title = ""
    seq_list = []
    for line in handle.readlines():
        line = line.strip()
        if line == "":
            continue
        if line[0] != ">":
            seq_list.append(line)
        else:
            title = line

seq = "".join(seq_list)
while True:
    position = input("Position: ")
    if position == "XXX":
        print("Okay, I will stop.")
        break
    else:
        position = int(position)
        seq_len = len(seq)
        if 1 <= position <= seq_len - 2:
            sliced_seq = seq[position - 1 : position + 2]
            print(f"Three amino acids: {sliced_seq}")
        else:
            print("Invalid range position value.")
