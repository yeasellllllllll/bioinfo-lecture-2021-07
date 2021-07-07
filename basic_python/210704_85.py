#! /usr/bin/env python
'''
#원의 둘레  구하는 함수 만들기

radius = input('radius: ')
def cir(radius):
    cir = float(2 * int(radius) * 3.141592)
    return cir

print('출력: ', cir(radius))
'''
'''
class Circle:

    def __init__(self,r):
        self.__r = r

    def r(self):
        return self.__r
    def area(self):
        return 3.14*float(self.r**2)
'''
sl = Circle(2)
print('area:{:0.2f}'.format(sl.area()))

