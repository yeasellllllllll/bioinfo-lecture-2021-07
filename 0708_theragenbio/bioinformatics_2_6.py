#! /usr/bin/env python

# a = input("Enter a string: ")

# print(f"Reversed string: {a[::-1]}")


def my_reverse(string):
    return string[::-1]


a = input("Enter a string: ")
reverse = my_reverse(a)
print(f"Reversed string: {reverse}")
