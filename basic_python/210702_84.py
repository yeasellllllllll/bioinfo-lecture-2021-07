#! /usr/bin/env python
'''
# 신규파일 생성 후 readline 하는 방법은???
FILE = open('./210702.txt', 'w')

FILE.write('Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat')


for i in FILE.readlines():      
    print(i)

FILE.close()
'''
'''
FILE = open('./test_file.txt', 'r')

for i in range(8):
    if i % 2 == 1:
        print(FILE.readlines(i)) #뭐지..........?

FILE.close()
'''

FILE = open('./test_file.txt', 'r')

line = FILE.readlines()

for i in range(8):
    if i % 2 == 1:
        print(line[i])

FILE.close()
