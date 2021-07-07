#! /usr/bin/env python

for i in [1, 2, 5]:
    print(i)
print('done!')

l_range = [1, 2, 5]

for i in l_range:
    print(i)
print('done!')

'''
for a in l_range:
    print(i)
print('done!')
a에대한 코멘트가 없기떄문에 에러가 발생한다
'''
i = '*'
for a in l_range:
    print(i)
print('done!')

'''
*
*
*
done!
'''
i = '*'
for a in l_range:
    print(a)
print('done!')

# TODO

print("보고싶은거")
l_range = [1, 2, 5]
for i in l_range:
    if i == 1: # indent required
        print(i)
    else :
        print('not 1!')      
    print('current :', i)
print('done!')
print("\n보고싶은2")
l_range = [1, 2, 5]
for i in l_range:
    print('current :', i)
    if i == 1: # indent required
        print(i)
    else :
        print('not 1!')      
print('done!')
print("보고싶은끝")

# 'not 1!' 쓰기싫을때, else 밑에 indent에 break를 넣으면 나오진 않지만 문제는 5를 확인한 결과는 나오지 않는다. list 5뒤에 1이 또있어도 확인을 하지 못한다. 
l_range = [1, 2, 5]
for i in l_range:
    print('current :', i)
    if i == 1: # indent required
        print(i)
    else :
        break      
print('done!')

# 두번째에 나오는 1도 확인하기 위해서! else뒤에 continue사용하기
# print('current :', i)의 위치에 따른 차이
l_range = [1, 2, 5, 3, 1, 7]
for i in l_range:
    if i == 1: # indent required
        print(i)
    else :
        continue 
    print('current :', i)
print('done!')

l_range = [1, 2, 5, 3, 1, 7]
for i in l_range:
    print('current :', i)
    if i == 1: # indent required
        print(i)
    else :
        continue 
print('done!')
