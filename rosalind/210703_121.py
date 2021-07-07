#! /usr/bin/env python
'''
#121
 # 1
h = input("")
print(h.upper())
 # 2
h = input("")
if h.islower():
    print(h.upper())
else:
    print(h.lower())

#122
score = input("score: ")

if 81 <= int(score) <= 100:
    print("grade is A")
elif 61 <= int(score) <= 80:
    print("grade is B")
elif 41 <= int(score) <= 60:
    print("grade is C")
elif 21 <= int(score) <= 40:
    print("grade is D")
elif 0 <= int(score) <= 20:
    print("grade is E")
else:
    print("incorrect score")

#123
d_won = {'달러':1167, '엔':1.096, '유로':1268, '위안':171}
h = input("입력(달러, 엔, 유로, 위안): ")
hs = h.split(' ')
#print(hs) -> h= 100 달러 -> ['100', '달러'] 
print(hs[0])
print(d_won[hs[1]])

print(int(hs[0]) * int(d_won[hs[1]]), "원")

# 수업 환율계산기

d_won =  {'USD':1203.82, 'EUR':1365.73, 'JPY':11.22, 'CNY':172.04}

won = "10 USD, 5 EUR, 7 JPY, 9 CNY"
l_won = won.split(',')

#print(l_won) ->  ['10 USD', ' 5 EUR', ' 7 JPY', ' 9 CNY']

usd = l_won[0].strip().split()
eur = l_won[1].strip().split()
jpy = l_won[2].strip().split()
cny = l_won[3].strip().split()

print(round(int(usd[0])* d_won[usd[1]], 2),"KRW, ",
int(eur[0])*d_won[eur[1]],"KRW, ",
int(jpy[0])*d_won[jpy[1]],"KRW, ",
int(cny[0])*d_won[cny[1]],"KRW")

#124
    # 내 답안
num1 = input('number1: ')
num2 = input('number2: ')
num3 = input('number3: ')

l_num = [num1, num2, num3]
ll_num = sorted(l_num)  
print(ll_num[2])

    # 답지
num1 = input('number1: ')
num2 = input('number2: ')
num3 = input('number3: ')
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

#125
    # 내 답안
d_num = {'011':'SKT', '016':'KT', '019':'LGU', '010':'알수없음'}
num = input("휴대전화 번호 입력(000-0000-0000): ")
numm = num.split('-') #리스트로 변경됨.
print(numm)
numm1 = d_num[numm[0]] #numm = d_num[num.split('-')[0]] 하나로 묶을 수 있음.
print(numm1)
print("당신은 {} 사용자 입니다.".format(numm1))

    # 답지
number = input("휴대전화 번호 입력(000-0000-0000): ")
num = number.split("-")[0]
print(num)
if num == '011':
    com = 'SKT'
elif num == '016':
    com = 'KT'
elif num == '019':
    com = 'LGU'
else:
    com = '알수없음'
print("당신은 {} 사용자 입니다.".format(com))

#126
num = input('우편번호: ')
numm = num[:3]
if num in ['010', '011', '012']:
    print('강북구')
elif num in ['014', '015', '016']:
    print('도봉구')
else:
    print('노원구')

#127
num = input('주민등록번호 (-표기): ')
numm = num.split('-')

if (numm[1][0]) in ['1', '3']:
    print('남자')
else:
    print('여자')

#128
num = input('주민등록번호 (-표기): ')
numm = num.split('-')[1]

#if 0 <= int(numm[1:3]) <= 8: # 답지
if int(numm[1:3]) in range(0,9,1): # 내답안
    print('서울 입니다.')
else:
    print('서울이 아닙니다.')

#129
num = input('주민등록번호 (-표기): ')
num1 = int(num[0])*2 + int(num[1])*3 + int(num[2])*4 + int(num[3])*5 + int(num[4])*6 + int(num[5])*7 + int(num[7])*8 + int(num[8])*9 + int(num[9])*2 + int(num[10])*3 + int(num[11])*4 + int(num[12])*5
num2 = 11 - (num1 % 11)
num3 = str(num2)
print(num1)
print(num2)
print(num3)

if num[-1] == num3[-1]:
    print('유효한 주민등록번호입니다.')
else:
    print('유효하지 않은 주민등록번호입니다.')
'''
#130


