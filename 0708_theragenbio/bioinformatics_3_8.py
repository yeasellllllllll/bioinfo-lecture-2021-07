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
# while True:
#     position = input("Searching for: ")
#     index = -1
#     l_index = []
#     if position == "XXX":
#         print("Okay, I will stop.")
#         break
#     else:
#         position = str(position)
#         while True:
#             index = seq.find(position, index + 1)
#             if index == -1:  # find()-> -1 더이상 찾는 문자 없는 경우
#                 break
#             l_index.append(str(index + 1))
#         s_index = ",".join(l_index)
#         print(f"Found at:{s_index}")
seq = "".join(seq_list)

l_index = []
while True:
    position = input("Searching for: ")
    if position == "XXX":
        print("Okay, I will stop.")
        break
    else:
        for i in range(len(seq)):
            if seq[i] == position:
                a = str(i + 1)
                l_index.append(a)
        s_index = ",".join(l_index)
        print(f"Found at: {s_index}")
