#! /usr/bin/env python
'''
#88 page
class Person:
    nation = 'A nation'
    
    def greeting(self):
        print('Hi')
    def printNation(self):
        print(self.nation)
    def changeNation(self, country):
        self.nation = country

yune = Person()
yune.greeting()
yune.printNation()
yune.changeNation('Korea')
print()
yune.printNation()
'''
'''
#89 page

class Person:
    nation = 'A nation' #속성 nation
    def greeting(self):    
    #def greeting(self, a): \n a.hi2() line 40을위해변경            
        #self = yune, yune의 greeting이 실행된다.
        print('(method)greeting:', 'Hi') 

    def hi1(self):                       #slef의 greeting 실행하는것
        self.greeting()
    def hi2(self):
        greeting()

def greeting():
    print('(funtion)greeting:', 'Hello!')   #class와 다른 독립적 아이

yune = Person()     #같은 class의 다른 instance
yune.greeting()
#yune.greeting(yune1)  -> (metho)greeting: Hi \n (funtion)greeting: Hello!로 출력됨.
yune.hi1()
yune.hi2()  
# hi2가 돌아가면 -> greeting()가 되고 greeting이 돌아가서 결국 Hello!가 나온다.
'''


#92page

class Person:
    def __init__(self, in_nation):
        self.nation = in_nation

    def showNation(self):
        print(self.nation)

yune = Person('Korea')  #instance를 여러개 생성할 수 있다는 예
yune1 = Person('AAA')

yune.showNation()
yune1.showNation()

'''
#93page

class Cat:
    def __init__(self):
        self.sleepy = True
    
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def snack(self):
        print("야옹")

catcat = Cat()
catcat.snack()
print(catcat.sleepy, end = '\n\n')

minyong = KoShort()
minyong.snack()
print(minyong.sleepy)
'''
'''
# 94page
class Cat:
    def snack(self):
        print('myeo~')

class KoShort(Cat):
    def setAge(self, Age):
        self.__age = Age        #self.__age (비공개속성)
        print('set age to ', Age)       

    def showAge(self):
        print(self.__age, 'years old.')

    def snack(self):
        print('야옹~')

minyong = KoShort()
minyong.setAge(7)
minyong.snack()
minyong.showAge()


#102 page

print('Try:')
try:
    print("aaaaaaa")
    print("aaaaaaa")
    print(minyong.__age)  #코드중에 어느 것이 에러가나도 except로 가서 표기해준다.
    print("bbbbbbb")     
    print("bbbbbbb")

#try중 어디가 에러났는지 정확히 알수 없다. 그래서 if문으로 쓰는 것이 더 현명한 방법이다!
except:
    print("Error!")
'''
