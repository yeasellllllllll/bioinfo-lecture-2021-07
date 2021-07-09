#! /usr/bin/env python

a = input("Enter a integer: ")
b = input("Enter another: ")

if int(a) > int(b):
    print(f"{a} is greater than {b}")
elif int(a) < int(b):
    print(f"{a} is less than {b}")
else:
    print(f"{a} is equal to {b}")
