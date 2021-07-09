#! /usr/bin/env python

# a = input("which times table: ")

# for i in range(1, 10):
#     print(f"{a} * {i} = {int(a)*i}")

# 강사님 답변
a = input("which times table: ")

if 0 < int(a) < 10:
    for i in range(1, 10):
        print(f"{a} * {i} = {int(a)*i}")
else:
    print("What?")
