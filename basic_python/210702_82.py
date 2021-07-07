#! /usr/bin/env python

'''
FILE = open('./test_file.txt', 'r')

# print(FILE.read(), end = '')    #전체가 읽힌다.


for i in FILE.readlines():  #['line0', 'line1', 'line2', ...]
    print(i.strip())


for i in FILE.readlines():  
    print(i.strip().split()[0])


FILE.close()
'''
'''
with open('./test_file.txt', 'r') as FI: 
    for i in FI.readlines():
        print(i.strip())                
    print('with out! Bye!')             
#with open으로 열면 마지막에 open한 파이를 닫아준다. FILE.close필요없다.
'''
'''
#list tuple dictionary 파일로 저장할때
"1,2,3,4"
string으로 바꿔서 저장하면 writh로 쓸수 있다.
'''

improt pickle

l_list = [1, 3, 5, 7]
d_dict = {'a':'A', 'b':'B', 1:3, 2:4}

FO = open(./pi_test', 'wb')          #pickle쓸때만 'wb'를 쓴다. 데이터 입력
pickle.dump(l_list, FO)
pickle.dump(d_dict, FO)
FO.cloase()


