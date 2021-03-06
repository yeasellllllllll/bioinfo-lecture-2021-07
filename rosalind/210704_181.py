#! /usr/bin/env python
#08.파이썬 반복문: 파이썬 for 문은 횟수가 정해져 있거나 상대적으로 횟수가 적은 경우에 대한 반복에 주로 사용됩니다. 파이썬 while문은 횟수가 상대적으로 크거나 무한 루프 형태의 반복문에 사용됩니다.
'''
#181
l_apart = [['101호', '102호'], ['201호', '202호'], ['301호', '302호']]

#182
l_a = ['시가', 100, 200, 300]
l_b = ['종가', 80, 210, 330]

#183
d_l = {'시가':'종가', [100, 200, 300]:[80, 210, 310]}

#184
d_stock = {'10/10':[80, 110, 70, 90], '10/11':[210, 230, 190, 200]}

#185
l_apart = [ [101, 102], [201, 202], [301, 302] ]

for i in l_apart:
    print(i[0],'호')
    print(i[1],'호')

#186
l_apart = [ [101, 102], [201, 202], [301, 302] ]
print(list(range(1,4)))

for i in range(1,4):

    print(l_apart[-i][0],'호')
    print(l_apart[-i][1],'호')

l_apart = [ [101, 102], [201, 202], [301, 302] ]
# 답지
for i in l_apart[::-1]:
    print(i[0],'호')
    print(i[1],'호')
    
#187
l_apart = [ [101, 102], [201, 202], [301, 302] ]

for i in l_apart[::-1]:
    print(i[1],'호')
    print(i[0],'호')
'''
#188
apart = [ [101, 102], [201, 202], [301, 302] ]
for row in apart:
    for col in row:
        print(col, "호")
        print("-" * 5)
#189


#190
