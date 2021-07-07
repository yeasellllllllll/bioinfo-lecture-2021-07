#! /usr/bin/env python

#081
a, b, *c = (0, 1, 2, 3, 4, 5)
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]

*valid_score, a, b= scores
print(valid_score)

#082
a, b, *valid_score = scores
print(valid_score)

#083
a, *valid_score, b = scores
print(valid_score)

#084
temp = {}
print(type(temp))

#085
test = {'메로나':1000, '폴라포':1200, '빵빠레':1800}
print(test)

#086
test['죠스바']=1200
test['월드콘']=1500
print(test)
test.update(a=1500, b=5800)
print(test)

#087
test = {'메로나':1000, '폴라포':1200, '빵빠레':1800, '죠스바':1200, '월드콘':1500}
print('메로나 가격: ', test['메로나'])

#088
test.update(메로나=1300)
print(test)

#089
del test['메로나']
print(test)

#090
icecream = {'폴라포':1200, '빵빠레':1800, '월드콘':1500, '메로나':1000}
#딕셔너리에 없는 것을 뽑을떄는 
