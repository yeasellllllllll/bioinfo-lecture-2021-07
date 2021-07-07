#! /usr/bin/env python

#071
my_variable = ()
print(type(my_variable))

#072
movie_rank = ('닥터 스트레인지', '스플릿', '럭키')

#073
my_tuple = (1, )
print(type(my_tuple))   #tuple

my_tuple = (1)
print(type(my_tuple))   #int

#074
# t = (1, 2, 3)
# t[0] ='a' #튜플은 내용을 변경할 수 없다.

#075
t = 1, 2, 3, 4 
print(type(t))

#077
interest = ('삼성전자', 'LG전자', 'SK Hynix')
list(interest)

#078
print(tuple(interest))

#079
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

#080
#(2, 4, 6, 8, ... 98)

temp = tuple(range(2, 100, 2))
print(temp)
