#! /usr/bin/env python

#201
def print_coin():
    print("비트코인")

#203
print_coin()

#204
for i in range(100):
    print_coin()

#205
def print_coins():
    for i in range(100):
        print("비트코인")

#206
def hello():
    print("Hi")
hello()
#함수가 정의되기 전에 호출시 에러 발생
#207
def message() :
    print("A")
    print("B")

message() 
#-> A \n B
print("C")
#-> C
message()
#-> A \n B

#208
print("A")

def message() :
    print("B")

print("C")
message()

#-> A \n C \n B

#209
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()

#-> A \n C \n B \n E \n D

#210
def message1():
    print("A")

def message2():
    print("B")

def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()

message3()

#-> B \n C \n B \n C \n B \n C \n A
