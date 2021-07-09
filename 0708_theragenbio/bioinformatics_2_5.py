#! /usr/bin/env python

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

# if (len(str(s1)) % 2 == 1) and (len(str(s1)) < len(str(s2))):
#     print(str(s1) + str(s2))
# else:
#     print(str(s2) + str(s1))

s1_len = len(str(s1))
s2_len = len(str(s2))
if (s2_len > s1_len) and (s1_len % 2 == 1):
    s3 = str(s1) + str(s2)
else:
    s3 = str(s2) + str(s1)
print(s3)
