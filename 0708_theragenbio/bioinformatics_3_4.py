#! /usr/bin/env python

# with open("sequence.protein.2.fasta", "w") as FI:
#     with open("sequence.protein.fasta", "r") as handle:
#         while True:
#             line = handle.readline()
#             if not line:
#                 break
#             linee = line.strip()
#             FI.writes(linee)

# with open("sequence.protein.2.fasta", "r") as handle:
#     while True:
#         line = handle.readline()
#         if not line:
#             break
#         print(line.strip())

# 강사님 방법
# with open("sequence.protein.fasta", "r") as handle:
#     seq_list = []
#     for line in handle.readlines():
#         line = line.strip()
#         if line == "":
#             continue
#         seq_list.append(line)

# seq = "\n".join(seq_list)
# with open("sequence.protein.2.fasta", "w") as FI:
#     FI.write("%s\n\n" % (seq))
#'%s\n' seq파일에는 리스트 하나하나 사이에 \n으로 줄이 구분되어 있으나
# 마지막 뒷부분에는 추가되어있지 않다. 기본 fasta파일에는 공백 2줄이 있기 때문에
# 파일을 동일하게 만들기 위해 2번 파이을 만들때 seq내용을 string으로 넣고
# 끝나는 부분의 2줄의 공백을 넣겠다 라는 이야기로 해석가능!!!

# 지온이 방법
with open("sequence.protein.fasta", "r") as handle:
    lines = handle.readlines()

with open("sequence.protein.2.fasta", "w") as FI:
    for line in lines:
        FI.write(line)
