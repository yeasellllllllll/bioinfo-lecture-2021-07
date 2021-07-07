#! /usr/bin/env python
'''
#151
l_d = [3, -20, -3, 44]

for i in l_d:
    if i > 0:
        continue
    else:
        print(i)
 
#152
l_d = [3, 100, 23, 44]

for i in l_d:
    if i % 3 == 0:
        print(i)

#153
l_d = [13, 21, 12, 14, 30, 18]

for i in l_d:
    if i % 3 == 0:
        if i < 20:
            print(i)

#모범 답안
for i in l_d:
    if (i < 20) and (i % 3 == 0):
        print(i)

#154
l_d = ['I', 'study', 'python', 'language', '!']

for i in l_d:
    if len(i) >= 3:
        print(i)

#155
l_d = ['A', 'b', 'c', 'D']

for i in l_d:
    if i.isupper() == True:
        print(i)

#156
l_d = ['A', 'b', 'c', 'D']

for i in l_d:
    if i.islower() == True:
    #if i.isupper() == False:
    #if i.isupper() != True:
    #if not i.isupper():
        print(i)
 
#157
l_d = ['dog', 'cat', 'parrot']

for i in l_d:
    print(i[0].upper() + i[1:])

#158
l_d = ['hello.py', 'ex01.py', 'intro.hwp']

for i in l_d:
    print(i.split('.')[0])

#159
l_d = ['intra.h', 'inra.c', 'define.h', 'run.py']

for i in l_d:
    if i.split('.')[1] == 'h':
        print(i)
''' 
#160
l_d = ['intra.h', 'inra.c', 'define.h', 'run.py']

for i in l_d:
    if (i.split('.')[1] == 'h') or (i.split('.')[1] == 'c'):
        print(i)


