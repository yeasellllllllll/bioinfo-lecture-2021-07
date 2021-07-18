#! /usr/bin/env python
# 41page
# A = "red apple"
# B = "yellow banana"

# print(B[:6] + " " + A[4:])
# print(A[:3] + " " + B[7:])

# 42page
# A = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain."
# print(A[22:28] + ' ' + A[97:103])
# print(A[22:28], A[97:103], sep=" ")

# 45page

# CMA = "1,234,567"

# print(int(CMA.replace(",", "")) + 100)

# 46page
# # 46_1.counting DNA nucleotides
# A = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

# print(A.count("A"))
# print(A.count("C"))
# print(A.count("G"))
# print(A.count("T"))

# # 46_2.Transcribing DNA into RNA
# DNA = "GATGGAACTTGACTACGTAAATT"
# print(f"RNA : {DNA.replace('T', 'U')}")

# 47page DNA nucleotide: complement
# A = "AAAACCCGGT"
# B = A[::-1]
# d_seq = {"A": "T", "T": "A", "G": "C", "C": "G"}
# # 방법1
# seq = []
# for i in B:
#     seq.append(d_seq[i])
# C = "".join(seq)
# print(C)
# # 방법2
# seq = ""
# for i in B:
#     seq += d_seq[i]
# print(seq)
# # 방법3
# D = B.replace("A", "t").replace("T", "a").replace("G", "c").replace("C", "g")
# print(D.upper())

# # 52page
# lang0 = ["python", "java"]
# lang1 = ["C", "C++", "VB"]
# totlaLang = lang0 + lang1
# print(totlaLang)

# # 56page
# regNum0 = "951213-0000000"
# regNum1 = "960125-0000000"
# regNum2 = "970705-0000000"
# d_mon = {
#     "01": "Jan",
#     "02": "Feb",
#     "03": "Mar",
#     "04": "Apr",
#     "05": "May",
#     "06": "Jun",
#     "07": "Jul",
#     "08": "Aug",
#     "09": "Sep",
#     "10": "Oct",
#     "11": "Nov",
#     "12": "Dec",
# }
# print(f"regNum0: {d_mon[regNum0[2:4]]}-{regNum0[4:6]}")
# print(f"regNum1: {d_mon[regNum1[2:4]]}-{regNum1[4:6]}")
# print(f"regNum2: {d_mon[regNum2[2:4]]}-{regNum2[4:6]}")

# # set (57page)
# A = [2, 6, 8, 9, 0, 2, 2, 8]
# B = set(A)  # {0, 2, 6, 8, 9}
# print(B)
# a = {2, 4, 6, 8, 10, 12}
# b = {9, 3, 12, 6}
# print(a | b)
# print(a & b)
# print(a ^ b)
# a.add(100)
# a.update({200})
# print(a)
# a.remove(100)
# print(a)

# # 59page
# # 답안 1
# test = "We tried list and we tried dicts also we tried Zen"
# l_test = test.split(" ")
# # ['We', 'tried', 'list', 'and', 'we', 'tried', 'dicts', 'also', 'we', 'tried', 'Zen']
# s_test = set(l_test)
# # {'also', 'Zen', 'dicts', 'we', 'We', 'and', 'tried', 'list'}
# d_test = {}
# for i in s_test:
#     print(i, l_test.count(i))
#     d_test[i] = l_test.count(i)
# print(d_test)
# print()  # 답안2
# test = "We tried list and we tried dicts also we tried Zen"
# l_test = test.split(" ")
# d_test = {}
# for i in l_test:
#     if i not in d_test:
#         d_test[i] = 1
#     else:
#         d_test[i] += 1
# print(d_test)

# # 66page 학점계산기
# score = int(input("입력 : "))
# if 90 <= score <= 100:
#     print("출력: A")
# elif 80 <= score <= 89:
#     print("출력: B")
# elif 70 <= score <= 79:
#     print("출력: C")
# elif 60 <= score <= 69:
#     print("출력: D")
# elif score <= 59:
#     print("출력: F")
# else:
#     print("숫자를 입력하세요.")

# # 67page, 환율계산기
# d_won = {"USD": "1203.82", "EUR": "1365.73", "JPY": "11.22", "CNY": "172.04"}
# won = "10 USD, 5 EUR, 7 JPY, 9 CNY"
# l_won = won.split(",")  # ['10 USD', ' 5 EUR', ' 7 JPY', ' 9 CNY']
# usd = l_won[0].strip().split()  # ['10', 'USD']
# eur = l_won[1].strip().split()  # ['5', 'EUR']
# jpy = l_won[2].strip().split()
# cny = l_won[3].strip().split()
# print(
#     int(usd[0]) * float(d_won[usd[1]]),
#     "KRW,",
#     int(eur[0]) * float(d_won[eur[1]]),
#     "KRW, ",
#     int(jpy[0]) * float(d_won[jpy[1]]),
#     "KRW, ",
#     int(cny[0]) * float(d_won[cny[1]]),
#     "KRW, ",
# )

# # 69page
# i = 1
# while True:
#     print("*" * int(i))
#     i += 1
#     if 6 < i:
#         break

# # 72 page
# gugu = input("입력: ")
# while not gugu.isdigit():
#     gugu = input("gugu is not digit!")
# gugu = int(gugu)
# for i in range(1, 9):
#     print(f"{gugu} * {i} = {i*gugu}")

# # 73 page
# # 100 ~ 200 사이의 모든 홀수 더하기
# # 방법 1
# total = 0
# for i in range(101, 200, 2):
#     total += i
# print(total)
# print()  # 방법 2
# instr = input("a(space)b: ")
# a, b = instr.split()
# my_list = []
# for i in range(int(a), int(b)):
#     if i % 2 == 1:
#         my_list.append(i)
# print(sum(my_list))
# print()  # 방법 3
# my_list = []
# for i in range(100, 200):
#     if i % 2 == 1:
#         my_list.append(i)
# print(sum(my_list))
# print()  # 방법 4
# print(sum(range(101, 200, 2)))

# # 74 page (palindromic sequence)
# test = input("입력: ")
# d_seq = {"A": "T", "T": "A", "G": "C", "C": "G"}
# test1 = test[::-1]
# outseq = ""
# for i in test1:
#     outseq += d_seq[i]
# if outseq == test):
#     print(f"{outseq} is palindromic.")
# else:
#     print(f"{outseq} is not palindromic.")

# # 79page(사칙연산 함수)
# # 1번 답안
# def calc(num0, num1, op):
#     if op == "+":
#         return f"{num0} {op} {num1} = {num0+num1}"
#     elif op == "-":
#         return f"{num0} {op} {num1} = {num0-num1}"
#     elif op == "/":
#         return f"{num0} {op} {num1} = {num0/num1}"
#     elif op == "*":
#         return f"{num0} {op} {num1} = {num0*num1}"
# cal1 = calc(5, 56, "*")
# cal2 = calc(5, 2, "+")
# print()
# print(cal1)
# print(cal2)

# # 80page 피보나치 수열
# n_fivo = int(input("n_th fivo (n<3): "))
# def fivo(n):
#     l_fivo = [0, 1]
#     for i in range(n - len(l_fivo)):
#         l_fivo.append(l_fivo[-1] + l_fivo[-2])
#     print(l_fivo[-1])
#     print(l_fivo)
# fivo(n_fivo)

# # 84page
# f = "./test_file.txt"
# with open(f, "r") as FI:
#     for idx, i in enumerate(FI.readlines()):
#         if idx % 2 == 1:
#             print(i.strip())

# # 85page
# radius = int(input("반지름 입력: "))
# def area(radius):
#     area = 3.141592 * radius ** 2
#     return area
# print(area(radius))

# # 91 page 사람 클래스 만들기
# class Person:
#     d_persons = {
#         "Guillaume": "Canada",
#         "Niklas": "Germany",
#         "Mark": "USA",
#         "Alex": "Swiss",
#         "Alberto": "Italia",
#     }
#     nation = "korea"
#     name = "me"
#     def __init__(self, name):
#         self.name = name
#     def setNation(self, nation):
#         self.d_persons[self.name] = nation
#     def showNation(self):
#         print(self.d_persons[self.name])

# g = Person("Guillaume")
# g.showNation()
# g.setNation("France")
# g.showNation()

# # 95 page
# class Student:
#     def __init__(self, korean, english, math):
#         self.__korean = korean
#         self.__english = english
#         self.__math = math
#         self.everage = (self.__korean + self.__english + self.__math) / 3

#     def showKorean(self):
#         print(self.__korean)

#     def showEnglish(self):
#         print(self.__english)

#     def showMath(self):
#         print(self.__math)

#     def showEverage(self):
#         print(self.everage)


# yune = Student(100, 90, 80)
# yune.showKorean()
# yune.showEnglish()
# yune.showMath()
# yune.showEverage()

# 96page 은행계좌 클래스!!!!
import random


class Account:
    def __init__(self, name, password, balance):
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)
        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def transfer(self, 수령인, amount):
        self.balance -= amount
        수령인.balance += amount

    def showBalance(self):
        print(self.balance)


me = Account("예슬", 1234, 50000)
you = Account("만섭", 5678, 3000)
print(me.account)
me.deposit(50000)
me.withdraw(5000)
me.transfer(you, 3000)
you.showBalance()
me.showBalance()
