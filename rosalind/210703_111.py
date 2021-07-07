#! /usr/bin/env python
'''
#111
h = "안녕하세요"
print(h * 2)

#112
h = 30
print(h + 10)

#113
h = input("num: ")
if int(h) % 2 == 0:
    print("짝수")
else:
    print("홀수")

#114
h = input("입력값: ")
if int(h) > 234:
    print("출력값: ",255)
else:
    print("출력값: ",int(h) + 20)

#115
h = input("입력값: ")
if int(h) < 20:
    print("출력값: ", 0)
elif int(h) > 275:
    print("출력값: ", 255)
else:
    print("출력값: ", int(h) - 20)
'
#116
h = input("현재시간(00:00): ")
if h[3:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")
'
#117
fruit = ["사과", "포도", "홍시"]
h = input("좋아하는 과일은? ")
if h in fruit:
    print("정답입니다.")
else:
    print("오답입니다.")

#118
warn_investment_list = ['Microsoft', 'Google', 'Naver', 'Kakao', 'SAMSUNG', 'LG']
h = input("종목명: ")

if h in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")

#119
fruit = {'봄':'딸기','여름':'토마토','가을':'사과'}
h = input("제가 좋아하는 계절은: ")

if h in fruit.keys():
    print("정답입니다.")
else:
    print("오답입니다.")
'''
#120
fruit = {'봄':'딸기','여름':'토마토','가을':'사과'}
h = input("제가 좋아하는 과일은: ")
if h in fruit.values():
    print("정답입니다.")
else:
    print("오답입니다.")

