#! /usr/bin/env python

chicken = 10 #전역변수

def countChicken(people):
    chicken = 20   #지역변수, 함수안에서 변수를 선언했기때문에
    chicken -= people
    print('{0} chicken remained.'.format(chicken))
def countChicken_global(people):
    global chicken  
    #global 이용하여 함수 내에서 접근 가능 (전역변수를 가져다 쓰겠다.)
    chicken = chicken - people
    print('{0} Chicken remained.'.format(chicken))

print('chicken:', chicken) #전역변수    chicken=10
countChicken(5)            #지역변수 사용, 전역변수 그대로  
print('chicken:', chicken) #전역변수, chicken 지역변수로 변경했으니 똑같이 10
print()
print('chicken:', chicken) #전역변수    chicken=10
countChicken_global(5)     #전역변수 수정 
print('chicken:', chicken) #전역변수    chicken=5
