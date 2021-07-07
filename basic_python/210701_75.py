#! /usr/bin/env python
'''
def showHello():
    print("Hello")
    return '1'       #반환이되서 string 자리에 1이들거가게한다.

showHello()          #->Hello
print(showHello())   #->Hello \n 1

a = showHello()      #->Hello
print("number?")     #->number?
print(a)             #->1


#76page
def add(a,b):
    print('add', a, 'and', b)
    print('%d + %d =' % (a,b), a+b)
    return a+b

result = add(3,4)
print('result:', result)

def hello() -> None: 
    print('hello!!!')

def add(a, b) -> int :
    return a+b

print(hello())

#78page
def add(a, b=3):
    return a+b

print(add(3))

#78 예제
def book_0(name, age, book1, book2):
    print('name: {0} age: {1}'.format(name, age), end = ' ')
    print('book:', book1, book2)

def book_1(name, age, *books):
    print('name: {0} age: {1}'.format(name, age), end =' ')
    print('book:', end = ' ')
    for book in books:
        print(book, end = ' ')
    print()

book_0('yune', 5, 'python', 'basic')
book_1('yune', 5, 'python', 'basic')
book_1('yune', 5, 'python', 'basic', 'photo')

book_1('yune', 5, 'python', 'basic', 'photo', 'a', 'ab')
'''

print('lambda:' (lambda a, b:a+b)(3,4))


