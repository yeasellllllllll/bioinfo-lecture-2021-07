#! /usr/bin/env python

# p = "title.txt"

# with open(p, "r") as handle:
#     lines = handle.readlines()
#     for line in lines:  # line -> string 자료형
#         line = line.strip()  # strip은 string만 사용가능
#         break

# print(f"The first line is : {line}")
# #readlines() 모두 다 읽어주는 것

# lines로 읽지말고 흠.......?

p = "title.txt"

with open(p, "r") as handle:
    for line in handle.readlines():
        line = line.strip()
        break

print(f"The first line is : {line}")
