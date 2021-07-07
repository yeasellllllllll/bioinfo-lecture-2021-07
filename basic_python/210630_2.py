#! /usr/bin/env python

#TODO 67page 환율계산기
inStr = '10 USD, 5 EUR, 7 JPY, 9 CNY'
d_value = {
            'USD':1203.82,
            'EUR':1365.73,
            'JPY':11.22,
            'CNY':172.04
            }

inStr = inStr.split(',')
print(inStr)
# ['10 USD', ' 5 EUR', ' 7 JPY', ' 9 CNY']

print(inStr[0].strip().split()[0]) #10
print(inStr[0].strip().split()[1]) #USD
print(inStr[1].strip().split()[0]) #5
print(inStr[1].strip().split()[1]) #EUR
print(inStr[2].strip().split()[0]) #7
print(inStr[2].strip().split()[1]) #JPY
print(inStr[3].strip().split()[0]) #9


#TODO

VALUE0 = inStr[0].strip().split()[0]
TYPE0 = inStr[0].strip().split()[1]
VALUE1 = inStr[1].strip().split()[0]
TYPE1 = inStr[1].strip().split()[1]
VALUE2 = inStr[2].strip().split()[0]
TYPE2 = inStr[2].strip().split()[1]
VALUE3 = inStr[3].strip().split()[0]
TYPE3 = inStr[3].strip().split()[1]

print(VALUE0, VALUE1, VALUE2, VALUE3)
print(TYPE0, TYPE1, TYPE2, TYPE3)

result0=int(VALUE0) * d_value[TYPE0]  
result1=int(VALUE1) * d_value[TYPE1]  
result2=int(VALUE2) * d_value[TYPE2]  
result3=int(VALUE3) * d_value[TYPE3]  

print(result0, result1, result2, result3)

'''
10 5 7 9
USD EUR JPY CNY
12038.199999999999 6828.65 78.54 1548.36
'''

result0=str(int(VALUE0) * d_value[TYPE0])  
result1=str(int(VALUE1) * d_value[TYPE1]) 
result2=str(int(VALUE2) * d_value[TYPE2]) 
result3=str(int(VALUE3) * d_value[TYPE3]) 

print(result0)

fruit = 'apple'
print(fruit.upper())

