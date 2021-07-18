"""전사와 역상보
1. 입력받은 DNA 서열의 전사한 RNA 서열을 출력하라.
2. 입력받은 DNA 서열에 역상보적인 서열을 출력하라."""

dna = input("seq: ")
rna = dna.replace("T", "U")
print("RNA :", rna)

d_base = {"A": "T", "G": "C", "C": "G", "T": "A"}
seqCom = ""
for i in dna[::-1]:
    seqCom += d_base[i]

print("Reverse Complement :", seqCom[::-1])
