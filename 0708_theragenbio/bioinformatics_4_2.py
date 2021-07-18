#! /usr/bin/env python

f = "sequence.protein.gb"

with open(f, "r") as handle:
    line_count = 0
    title = ""
    seq_list = []
    origin_start = False
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

print(f"title: {title}")
seq_str = " ".join(seq_list)
seq_s = seq_str.replace(" ", "")
seq_str = []
for i in seq_s:
    if i.isalpha() == True:
        seq_str.append(i)
    else:
        pass

s_sstr = "".join(seq_str)
print(f"seq: {s_sstr}")
