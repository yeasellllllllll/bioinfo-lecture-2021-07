#! /usr/bin/env python

# a = input("Enter a string: ")

# print(f"The string length is {len(str(a))}")


def my_len(string):
    cnt = 0
    for s in string:
        cnt += 1
    return cnt


a = input("Enter a string: ")
length = my_len(a)
print(f"The string length is {length}")
