#! /usr/bin/env python

f = "sequence.protein.gb"

with open(f, "r") as handle:
    for line in handle.readlines():
        line = line.strip()
        seq_list = []
        if line.startswith("ORIGIN"):
            seq_list = line.strip().append()

        break
