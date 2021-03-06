#! /usr/bin/env python

f = "sequence.protein.gb"

with open(f, "r") as handle:
    line_count = 0
    title = ""
    seq_list = []
    origin_start = False  # origin_flag 스위치 on off 형태이다.
    for line in handle.readlines():
        line = line.strip()
        if line == "":
            continue
        elif line_count == 0:
            title = line
        elif line.startswith("ORIGIN"):
            origin_start = True
        elif origin_start == True:
            seq_list.append(line)
        line_count += 1

seq = "\n".join(seq_list)
print(f"title: {title}")
print(f"seq: {seq}")
