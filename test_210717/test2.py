# 2. 입력받은 DNA 서열이 이의 상보적 서열과 같은지 확인하라.

# a = input("DNA Seq.: ")
# a_r = a[::-1]
# a_rc = a.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
# b = a_rc.upper()
# print(b)

# if a == b:
#     print("True")
# else:
#     print("False")

# 방법 2
seq = input("DNA Seq.: ")
d_base = {"A": "T", "G": "C", "C": "G", "T": "A"}
seqCom = ""
for i in seq[::-1]:
    seqCom += d_base[i]

if seq == seqCom:
    print("True")
else:
    print("False")
