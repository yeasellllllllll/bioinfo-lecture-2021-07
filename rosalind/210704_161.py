#! /usr/bin/env python
'''
#161
i = 0
for i in range(100):
    print(i)

#162
print(list(range(2002, 2051, 4)))

#163
i = 0
for i in range(3, 31, 3):
    print(i)

#164
print(list(range(99, -1, -1))) #list로 출력됨

#답지, 한라인에 하나씩 출력됨
i = 0
for i in range(100):
    print(99 -i)

#165
i = 0
for i in range(10):
    print(i / 10)

#166
i = 0
for i in range(1, 10):
    print('3x{} = {}'.format(i, int(3*i)))

#class 72page 구구단 출력하기
gugu = input('gugu?')

for i  in range(1,10):
    print('{} * {} = {}'.format(gugu, i, int(i)*int(gugu)))

#167
i = 0
for i in range(1, 10, 2):
    print('3x{} = {}'.format(i, int(3*i)))
#답지
num = 3
for i in range(1,10):
    if i % 2 == 1:
        print(num, 'x', i, '=', num*i)

#168
l_d = list(range(1,11))
print(sum(l_d))

#답지
hab = 0
for i in range(1,11):
    hab += i
print(hab)

#169
l_d = list(range(1,11,2))
print(sum(l_d))

#답지
hab = 0
for i in range(1,11,2):
    hab += i
print(hab)
'''
#170
dd = 1
for i in range(1,11):
    dd *= i
print(dd)      

