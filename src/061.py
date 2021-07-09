f = "061.fastq"
cnt = 0  # cnt = count
data = {}

with open(f, "r") as handle:
    for line in handle:
        if cnt % 4 == 0:  # header
            pass
        elif cnt % 4 == 1:  # base
            for base in line.strip():
                if base not in data:
                    data[base] = 0
                data[base] += 1
        elif cnt % 4 == 2:  # delimiter
            pass
        elif cnt % 4 == 3:  # equal
            pass
        cnt += 1

print(cnt / 4)
print(data)
