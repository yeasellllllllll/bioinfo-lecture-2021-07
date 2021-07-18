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

lseq_70 = []
for i in range(0, len(s_sstr), 70):
    lseq_70.append(s_sstr[i : i + 70])

sseq_70 = "\n".join(lseq_70)
print(sseq_70)
