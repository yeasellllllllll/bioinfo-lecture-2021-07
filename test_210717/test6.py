"""번역 (sequence_DNA.txt 파일로 진행해보기)
1. 입력받은 서열을 아미노산 서열로 번역 출력하라.
2. 주어진 아미노산을 암호화하고 있는 각 코돈의 비율을 DNA 서열로 표현
결과를 사전으로 반환하며 사전의 키는 코돈이고 값은 코돈의 사용빈도를 나타낸다."""

codon_dic = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "*",
    "TAG": "*",
    "TGT": "C",
    "TGC": "C",
    "TGA": "*",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}

# 1. 입력받은 서열을 아미노산 서열로 번역 출력하라.
# f = "./sequence_DNA.txt"

# with open(f, "r") as handle:
#     for i in handle.readlines():
#         seq = i.strip()
#         amino_acid = ""
#         for n in range(0, len(i.strip()), 3):
#             if len(seq[n : n + 3]) == 3:
#                 amino_acid += codon_dic[seq[n : n + 3]]
#             else:
#                 continue
# print(amino_acid)

# 2. 주어진 아미노산을 암호화하고 있는 각 코돈의 비율을 DNA 서열로 표현
# 결과를 사전으로 반환하며 사전의 키는 코돈이고 값은 코돈의 사용빈도를 나타낸다.

f = "./sequence_DNA.txt"

with open(f, "r") as handle:
    for i in handle.readlines():
        seq = i.strip()
        amino_acid = {}
        for n in range(0, len(i.strip()), 3):
            if len(seq[n : n + 3]) == 3:
                if codon_dic[seq[n : n + 3]] not in amino_acid:
                    amino_acid[codon_dic[seq[n : n + 3]]] = 1
                else:
                    amino_acid[codon_dic[seq[n : n + 3]]] += 1
            else:
                continue
print(amino_acid)
