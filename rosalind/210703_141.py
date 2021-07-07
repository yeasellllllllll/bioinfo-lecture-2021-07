#! /usr/bin/env python
'''
#141
l_d = [100, 200, 300]

for i in l_d:
    print(i + 10)

#142
l_d = ['김밥', '라면', '튀김']

for i in l_d:
    print("오늘의 메뉴: ", i)

#143
l_d = ['SK하이닉스', '삼성전자', 'LG전자']

for i in l_d:
    print(len(i))

#   count(i)는 i가 몇개 있는 지 세어줘, len은 몇글자인지 알려줘

#144
l_d = ['dog', 'cat', 'parrot']

for i in l_d:
    print(i, len(i))

#145
l_d = ['dog', 'cat', 'parrot']
print(l_d[0][0])
for i in l_d:
    print(i)
    print(i[0])

#146
l_num = [1, 2, 3]

for i in l_num:
    print('3 x', i)

#147
l_num = [1, 2, 3]

for i in l_num:
    print('3 x', i,'=', int(i*3))
#    print('3 x {} = {}'.format(i, 3*i))

#148
l_d = ['가', '나', '다', '라']
l_dd = l_d[1:]
# 내방법
for i in l_d:
    if i == '가':    
        continue
    else:
        print(i)
# 답지 1
for i in l_dd:
    print(i)
# 답지 2***
for i in l_d[1:]:
    print(i) 

#149
l_d = ['가', '나', '다', '라']

for i in l_d[::2]:
    print(i)
''' 
#150
l_d = ['가', '나', '다', '라']

for i in l_d[::-1]:
    print(i)

