# f = "070.vcf"

# line = 0
# with open(f, "r") as handle:
#     for i in handle:
#         if i.startswith("#"):
#             continue
#         else:
#             line += 1
# print(line)

# 070.vcf 파일에서 FILTER 열이 PASS인 행의 개수를 구하라
f = "070.vcf"
cnt_all = 0
cnt_pass = 0

with open(f, "r") as handle:
    for i in handle:
        if i.startswith("##"):
            continue
        elif i.startswith("#"):
            header = i.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = i.strip().split("\t")
        cnt_all += 1
        if data[filter_idx] == "PASS":
            cnt_pass += 1

print(cnt_pass, cnt_all, cnt_pass / cnt_all)
