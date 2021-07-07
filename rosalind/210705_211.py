#! /usr/bin/env python

#211
def 함수(문자열) :
    print(문자열)

함수("안녕") #안녕
함수("Hi")   #Hi

#212
def 함수(a, b) :
    print(a + b)

함수(3, 4) #7
함수(7, 8) #15

#213
def 함수(문자열) :
    print(문자열)
#함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.

#214
def 함수(a, b) :
    print(a + b)

#함수("안녕", 3)
#string과 int는 더할 수 없다.

#215
def print_with_smile(string):
    print(string + ":D")

#216
def print_with_smile(string):
    print(string + ":D")

print_with_smile("안녕하세요")
#217
def print_upper_price(a):
    print(a*1.3)

#218
def print_sum(a, b):
    print(a+b)

#219
def print_arithmetic_operation(a, b):
    print(a, "+", b, "=", a+b)
    print(a, "-", b, "=", a-b)
    print(a, "*", b, "=", a*b)
    print(a, "/", b, "=", a/b)

print_arithmetic_operation(3, 4)

#220
def print_max(a, b, c):
    print(max(a, b, c))
print_max(5, 9, 58)

# 220 답지
def print_max(a, b, c):
    max_val = 0
    if a > max_val:
        max_val = a
    if b > max_val:
        max_val = b
    if c > max_val:
        max_val = c
    print(max_val)
print_max(5, 9, 58)
