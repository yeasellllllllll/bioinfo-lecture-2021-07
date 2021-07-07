#! /usr/bin/env python

#101
#파이썬에서 True or False를 갖는 type -> type입니다

#102
print(3 == 5) #False

#103
print(3 < 5) #True

#104
x = 4
print(1 < x < 5) #True

#105
print((3==3) and (4 != 3)) #True
#!= 같지 않으면 true 같으면 False

#106
#print(3 => 4)
#<, >, ==, !=, >=, <=, and, or, not, in 만가능
#>= 이렇게 부등호 먼저 =가 나중에 나오면 문제없이 출력된다.

#107
if 4<3:
    print("Hello World")
#아무 결과 출력x

#108
if 4<3:
    print("Hellow World.")
else:   
    print("Hi, there.")
#Hi, there.

#109
if True :
    print("1")
    print("2")
else:
    print("3")
print("4")
#1\n 2\n 4\n

#110
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print('4')
print("5")


