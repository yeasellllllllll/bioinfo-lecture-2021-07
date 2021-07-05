#! /usr/bin/env python

#반지름을 나타내는 변수 r을 사용하여 원의 넓이를 구해봅시다.
'''
r = int(input("r ="))

area = float(3.14 * r **2)
print("area =", area)


#강사님답1
import math

r = 2
pi = math.pi
result = round(r**2 * pi, 2) 
#round(받을수, 2) 소수점 2번째 자리까지 표기

print(result)
'''
#강사님답2
import math
import sys

r = int(sys.argv[1]) 
pi = math.pi
result = round(r**2 * pi, 2) 

print(result)

