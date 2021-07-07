#! /usr/bin/env python

#231
def n_plus_1 (n) :
    result = n + 1

n_plus_1(3)
#print (result) #4  xxxxx
# 에러발생함 : 함수 내에서 사용한 변수는 함수밖에서 접근 x
# 함수밖에서 접근하려면 return으로 지정되야 한다.

#232
def make_url(string):
    print("www."+string+".com")

make_url("naver")

#233
'''
def make_list(string):
    print(list(string))

make_list("abcd")
'''
def make_list(string):
    my_list = []
    for i in string:
        my_list.append(i)
#        print(my_list)
    print(my_list)

make_list("abcd")

#234
def pickup_even(l_num):
    result = []
    for i in l_num:
        if i % 2 == 0:
            result.append(i)
    print(result)

pickup_even([3, 4, 5, 6, 7, 8])

#235
def convert_int(num):
    print(int(num.replace(',','')))
  
convert_int("1,234,567")
'''
#236
def 함수(num) :
    return num + 4

a = 함수(10) #14
b = 함수(a)  #18
c = 함수(b) #22
print(c) # -> 22

#237
def 함수(num) :
    return num + 4

c = 함수(함수(함수(10)))
print(c) 

#238
def 함수1(num) :
    return num + 4

def 함수2(num) :
    return num * 10

a = 함수1(10) -> 14
c = 함수2(a) -> 140
print(c) ->140

#239
def 함수1(num) :
    return num + 4

def 함수2(num) :
    num = num + 2
    return 함수1(num)

c = 함수2(10)
print(c)

#240
def 함수0(num) :
    return num * 2

def 함수1(num) :
    return 함수0(num + 2)

def 함수2(num) :
    num = num + 10
    return 함수1(num)

c = 함수2(2)
print(c)
'''
