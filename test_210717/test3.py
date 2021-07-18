"""3. 입력받은 DNA 서열에서 대문자로 변환하여 ①각 문자의 출현 빈도를 계산하고 ② 각 뉴
클레오티드를 퓨린과 피리미딘으로 나눠 그 개수를 세라.
>> 결과값 : 각 염기의 개수를 사전형태로 출력"""

seq = input("seq.: ")
seq_u = seq.upper()
d_seq = {}
for i in seq_u:
    if i not in d_seq:
        d_seq[i] = 1
    else:
        d_seq[i] += 1

print(d_seq)
print("purine =", seq_u.count("A") + seq_u.count("G"))
print("pyrimidine =", seq_u.count("T") + seq_u.count("C"))
