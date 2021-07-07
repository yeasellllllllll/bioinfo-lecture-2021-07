#! /usr/bin/env python

# while, append, sum 하면 ?????
# 강사님 모범 답안


#1 (use list and .append)
n_pivo = int(input('n_th pivo:  '))
l_pivo = [0, 1]     #n_th pivo: l_pivo[n]
print('len(l_pivo): ', len(l_pivo))


def pivo(n):            
    while len(l_pivo) < n: #while안에 조건문이 참일때까지 계속 반복
        l_pivo.append(l_pivo[-1] + l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)
pivo(n_pivo)

'''
#2 while 대신에 for쓸경우
n_pivo = int(input('n_th pivo (n<3): ')
l_pivo = [0, 1]     #n_th pivo: l_pivo[n]
print('len(l_pivo): ', len(l_pivo))

def pivo(n):            
    for i in range(n - len(l_pivo)):
        l_pivo.append(l_pivo[-1] + l_pivo[-2])
    print(l_pivo[-1])
    print(l_pivo)
pivo(n_pivo)
'''
'''
#3 재귀호출이용 함수 방법, def안에서 def자신을 호출하는 것(에러주의)
n_pivo = int(input('n_th pivo : ')
l_pivo = [0, 1]     #n_th pivo: l_pivo[n]
print('len(l_pivo): ', len(l_pivo))

def pivo_r(n):
    if n == 0
        return 0
    elif n == 1
        return 1
    else:
        return pivo_r(n-1) + pivo_r(n-2)
print('pivo_r:', pivo_r(n_pivo -1))
'''
'''
#4 그냥 쓰고 진행x
d_pivo = {0:0, 1:1, 2:1}
def pivo_d(n):
    if n in d_pivo:
        return d_pivo[n]
    else:
        if d_pivo[n] = d_pivo[n-1] + d_pivo[n-2]
    return d_pivo[n]

print('pivo_d:', pivo_d(n_pivo
'''
