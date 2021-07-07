#! /usr/bin/env python

seq = 'AAAACCCGGT'
d_nucl = {'A':'T','T':'A','G':'C','C':'G'}

seq1 = ''
for i in seq[::-1]:
    seq1 += d_nucl[i]
print(seq1)

#replace 사용방법

r_seq = seq[::-1]
c_seq = r_seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g')

print(c_seq.upper())



