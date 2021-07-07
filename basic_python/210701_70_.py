#! /usr/bin/env python

print(list(range(5)))
# [0, 1, 2, 3, 4]

print('hello'[::-1])
# olleh

print('0123456789'[0:5:1])
#위의 숫자 위치 찾는 것은 원하는 위치를 설정할수없다.

print(list(range(2, 5, 1)))
# [2, 3, 4] 2~5사이의 1차이나게끔 올려서 리스트 보여줘

totalSum = 0
for i in range(3):
    totalSum += i
    print(i)

print('totalSum:', totalSum)

'''
0
1
2
totalSum: 3
'''
for i in range(3):
    if i == 2:
        print(i)
    else:
        pass
print('totalSum:', totalSum)

totalSum = 0
for i in range(3):
    if i == 2:
        print(i)
    else:
        continue
print('totalSum:', totalSum)

totalSum = 0
for i in range(3):
    if i == 2:
        print(i)
    else:
        break
print('totalSum:', totalSum)

