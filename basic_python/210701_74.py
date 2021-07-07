#! /usr/bin/env python
'''
#내꺼!
seq = input('seq: ')
d_nucl = {
        'A':'T',
        'T':'A',
        'G':'C',
        'C':'G'
        }
out_seq = ''

for i in seq[::-1]:
    out_seq += d_nucl[i]
if (out_seq == seq):
    print(seq,' is palindromic.')
else:
    print(seq, ' is not palindromic.') 
'''
'''
# replace는 어떻게 하는 걸까?
seq = input('seq: ')

r_seq = seq[::-1]
c_seq = r_seq.replace('A','t'),('T','a'),('G','g'),('C','c')
print(c_seq)
'''

'''
#강사님 답
inSeq = input('Give Me Sequence!: ')
d_nucl = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
outSeq = ''
for i in inSeq[::-1]:
    outSeq += d_nucl[i]
if (outSeq == inSeq):
    print('{} is palindromic'.format(inSeq))
else:
    print('{} is not palindromic'.format(inSeq))
'''

inSeq = input('Give Me Sequence!: ')
d_nucl = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

print(range(len(inSeq)))

for i in range(len(inSeq)):
    if(inSeq[i] == d_nucl[inSeq[-i-1]]):
        print("okay~")
    else:
        print("Not palindrom!")
