#! /usr/bin/env python

# f = "sequence.protein.2.fasta"

# with open(f, "r") as handle:
#     title = ""
#     seq_list = []
#     for line in handle.readlines():
#         line = line.strip()
#         if line == "":
#             continue
#         if line[0] != ">":  # 라인의 첫번째 문자가 >이 아니면
#             seq_list.append(line)
#         else:
#             title = line
# seq = "".join(seq_list)
# print(f"title: {title}")
# print(f"seq: {seq}")


f = "sequence.protein.2.fasta"

with open(f, "r") as handle:
    title = ""
    seq_list = []
    for line in handle.readlines():
        line = line.strip()
        if line == "":
            continue
        elif line.startswith(">") != True:
            seq_list.append(line)
        else:
            title = line

seq = "".join(seq_list)
print(f"title: {title}")
print(f"seq: {seq}")
