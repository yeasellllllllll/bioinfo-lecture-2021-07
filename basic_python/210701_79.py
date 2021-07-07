#! /usr/bin/env python

#내꺼 답안1

op_list = {'add':'+','substact':'-','multiply':'*','divide':'/'}

def calc(num0, num1, op):
#    print('{}, op_list[op], {}'.format(num0, num1))
    print('{} {} {}'.format(num0, op_list[op] ,num1))
    return eval(str(int(num0))+ str(op_list[op])+ str(int(num1)))

print( eval(" 10 + 100")    )

result = calc(5, 6,'add')  
print('result', result)


'''
def calc(num0, num1, op):
    if op == '+':
        print('%d + %d =' %(num0, num1), int(num0) + int(num1))
        return int(num0) + int(num1)
    elif op == '-':
        print('%d - %d =' %(num0, num1), int(num0) - int(num1))
        return int(num0) - int(num1)
    elif op == '*':
        print('%d * %d =' %(num0, num1), int(num0) * int(num1))
        return int(num0) * int(num1)
    elif op == '/':
        print('%d / %d =' %(num0, num1), int(num0) / int(num1))
        return int(num0) / int(num1)

calc(7, 5, '*')
'''

'''
i=input('num op num = ')
l=i.split(' ')

num0=int(l[0])
op=l[1]
num1=int(l[2])

def clac(num0,num1,op):
    if op == '+':
        print(f'{num0} {op} {num1} = {num0+num1}')
        return int(num0) + int(num1)
    elif op == '-':
        print(f'{num0} {op} {num1} = {num0-num1}')
        return int(num0) - int(num1)
    elif op == '*':
        print(f'{num0} {op} {num1} = {num0*num1}')
        return int(num0) * int(num1)
    elif op == '/':
        print(f'{num0} {op} {num1} = {num0/num1}')
        return int(num0) / int(num1)

result = clac(num0,num1,op)
print('result :', result)
'''
'''
#강사님 모범답안 1
def calc(num0, num1, op):
    print('{} {} {}'.format(num0, num1, op))
    if op == '+':
        result = num0 + num1
        return result
    elif op == '-':
        result = num0 - num1 
        return result  
 #함수에서 리턴은 한번만 되기 때문에 if 안에 있을때는 해당하는 사칙연산만 진행 후 나가는 것이고 return을 마지막에 if끝에 넣으면 모두다 진행 후 return된다.
    elif op == '*':
        result = num0 * num1
        return result
    elif op == '/':
        result = num0 / num1
        return result

cal1 = calc(5, 56, '*')
cal2 = calc(5, 2, '-')
print(cal1)
print(cal2)
'''
'''
# 강사님 모범답안 2
def calc(num0, num1, op):
    print('{} {} {}'.format(num0, num1, op))
    if op == '+':
        return num0 + num1
    elif op == '-':
        return num0 - num1 
    elif op == '*':
        return num0 * num1
    elif op == '/':
        return num0 / num1

cal1 = calc(5, 56, '*')
cal2 = calc(5, 2, '-')
print(cal1)
print(cal2)
'''
