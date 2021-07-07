seq = 'ATGTTATAG'
comp_seq = ""
comp_data = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

for i in seq:
    comp_seq += comp_data[i]

print(seq)
print(comp_seq)

for i in range(len(seq)):
    s = seq[i]
    cs = comp_seq[i]
    bond = "≡"
    if s == "A" or s == "T":
        bond = "="
    print(f"{s}{bond}{cs}")
