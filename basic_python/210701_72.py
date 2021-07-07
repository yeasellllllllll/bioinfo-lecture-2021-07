#! /usr/bin/env python

'''
망한풀이

gugu = int(input('구구단: '))

for gugu in range(2, 19, 1):
    dan += 1
    print('{} * {}'.format(int(gugu), int(dan))
    if 9 < i :
        break
''' 
# 강사 답안 1

gugu = input('gugu?')

while not gugu.isdigit():
    gugu = input('gugu is not digit!:')
   
#숫자가 날때 에러가 나는 것을 방지하기 위해서 숫자만 들어가라! 숫자일때까지

gugu = int(gugu)

for i in range(1,10):
    dan = i * gugu
    print('{} * {}: {}'.format(gugu, i, dan))

