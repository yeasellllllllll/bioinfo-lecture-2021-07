#! /usr/bin/env python

# 291
f = "매수종목1.txt"
with open(f, "w") as handle:
    handle.write("005930\n")
    handle.write("005380\n")
    handle.write("035420")

# 292
f = "매수종목2.txt"
with open(f, "w") as handle:
    handle.write("005930 삼성전자\n")
    handle.write("005380 현대차\n")
    handle.write("035420 NAVER")

# 294
f = "매수종목1.txt"
with open(f, "r") as handle:
    l_dd = []
    for line in handle.readlines():
        code = line.strip()
        l_dd.append(code)
    print(l_dd)

# 295
f = "매수종목2.txt"
with open(f, "r") as handle:
    d_aa = {}
    for line in handle.readlines():
        code = line.strip()
        k, v = code.split(" ")
        d_aa[k] = v
    print(d_aa)

# 296
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except ValueError:
        print(0)

# 297
per = ["10.31", "", "8.00"]
l_per = []

for i in per:
    try:
        l_per.append(float(i))
    except ValueError:
        l_per.append(0)
print(l_per)

# 299
data = [1, 2, 3]

for i in range(5):
    try:
        print(data[i])
    except IndexError:
        print("err")

# 300
# try:
#     실행 코드
# except:
#     예외가 발생했을 때 수행할 코드
# else:
#     예외가 발생하지 않았을 때 수행할 코드
# finally:
#     예외 발생 여부와 상관없이 항상 수행할 코드
