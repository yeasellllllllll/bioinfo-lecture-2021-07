#! /usr/bin/env python

class Person:
    d_persons = {'Guillaume':'Canada', 'Niklas':'Germany', 'Mark':'USA', 'Ales':'Swiss', 'Alberto':'Italia'}
    nation="korea"
    name = "me"
    def __init__(self, n):
        self.name = n
    def setNation(self, x):
        self.d_persons[self.name] = x
    def showNation(self):
        print(self.d_persons.get(self.name))

g = Person('Guillaume')
g.showNation()
g.setNation('France')
g.showNation()
