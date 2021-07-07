#! /usr/bin/env python
'''
#강사님 방법
total = 0
for i in range(101, 200, 2):
    total =+ i
print(total)

# 방법 2
myList = []
for i in range (100, 200, 2):
    if i % 2 == 1:
        myList.append(i)
print(sum(myList))

# 방법 3
print(sum(range(101, 200, 2)))
'''


'''
#내가 풀고싶은 방법 + 강사님 설명

inStr = input('a(space)b:')
a, b = inStr.split()

myList = []
for i in range(int(a), int(b)):
    if i % 2 == 1:
        myList.append(i)
print(sum(myList))
'''

odd_integer = input('a(sapce)b:')
a, b = odd_integer.split()

total = 0
for i in range(int(a)+1, int(b), 2):
    total += i
print(total)

