f = "077.bed"

length = 0

with open(f, "r") as handle:
    for line in handle:
        chrom_start_end = line.split("\t")
        start = int(chrom_start_end[1])
        end = int(chrom_start_end[2])
        length += end - start


result = 0
print(length)

with open(f, "r") as handle:
    for line in handle:
        data = line.strip().split("\t")  # ['chr21', '10959722', '10959817']
        chrom, start, end = data
        length = int(end) - int(start)
        result += length

print(result)
