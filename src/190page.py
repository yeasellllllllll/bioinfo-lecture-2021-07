f = "data.txt"
d = {}
with open(f, "r") as fr:
    for line in fr:
        l = line.strip().split(" ")
        gene, val = l[0], l[1]
        d[gene] = val
print(d.items())
print(sorted(d.items(), key=lambda x: x[1], reverse=True))
