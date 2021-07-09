#! /usr/bin/env python

# f = "sequence.protein.2.fasta"

# with open(f, "r") as handle:
#     line_count = 0
#     line = handle.readlines()
#         line = line.strip()
#         if line_count == 1:
#             break
#         line_count += 1

# print(f"The second line is: {line}")

# 방법 1
f = "sequence.protein.2.fasta"
with open(f, "r") as handle:
    line_count = 0
    for line in handle.readlines():
        line = line.strip()
        if line_count == 1:
            break
        line_count += 1

print(f"The second line is: {line}")

# 방법 2
f = "sequence.protein.2.fasta"
with open(f, "r") as handle:
    for i in range(2):
        data = handle.readline()
    print(data)
