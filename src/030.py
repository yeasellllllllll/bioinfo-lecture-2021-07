seq = "AGTTTATAG"

for i in range(len(seq)):
    s = seq[i:i+2]
    print(i, s, s=="TT")

seq = "AGTTTATAG"

for i in range(len(seq)):
    s = seq[i:i+2]
    if s == "TT":
        print(i)

seq = "AGTTTATAG"
data = []

for i in range(len(seq)):
    s = seq[i:i+2]
    if s == "TT":
        data.append(i)
print(data)
