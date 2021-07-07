#! /usr/bin/env python

class Student:
    
    def __init__ (self, korean, english, math):
        self.__korean = korean
        self.__english = english
        self.__math = math
        
        self.total = korean + english + math
        self.average = self.total/3

    def showKorean(self):
        print(self.__korean)
    def showEnglish(self):
        print(self.__english) 
    def showMath(self):
        print(self.__math)
    def showAverage(self):
        print(self.average)
#print("%.2f"%((self.__korean + self.__english + self.__math)/3))
#average 하나로 묶는 방법
me = Student(int(input("korean: ")), int(input("english: ")), int(input("math: ")))


me.showKorean()
me.showMath()
me.showEnglish()
me.showAverage()
