#! /usr/bin/env python

f = "sequence.protein.fasta"

# with open(f, "r") as handle:
#     handles = handle.readlines()
#     for i in handles:
#         data = i.strip()
#         print(data)

# with open(f, "r") as handle:
#     while True:
#         line = handle.readline()
#         if not line:
#             break
#         print(line.strip())

# 강사님 답안
with open(f, "r") as handle:
    for line in handle.readlines():
        line = line.strip()
        if line == "":
            continue
        print(line)
        # 여기가 아니라 for 밖에서 print하게 되면 마지막 줄만 나온다!!!
