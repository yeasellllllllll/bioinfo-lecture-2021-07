#! /usr/bin/env python

# # 271
# import random

# class Account:
#     def __init__(self, name, balance):
#         self.name = name
#         self.blance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(1, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3

# kim = Account("김민수", 100)
# print(kim.name)
# print(kim.blance)
# print(kim.bank)
# print(kim.account_num)

# 272
# import random
# class Account:
#     all_account = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.blance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(1, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3

#         Account.all_account += 1

# kim = Account("김민수", 100)
# print(kim.name)
# print(kim.blance)
# print(kim.bank)
# print(kim.account_num)
# print(Account.all_account)

# 273
# import random


# class Account:
#     all_account = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.blance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(1, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account_num = num1 + "-" + num2 + "-" + num3

#         Account.all_account += 1

#     def get_account_num(cls):  # class 매소드 (객체접근필요x)
#         print(cls.all_account)  # cls = class


# kim = Account("김민수", 100)
# lee = Account("이민수", 100)
# kim.get_account_num()

# 274, 275
# import random


# class Account:
#     all_account = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account = num1 + "-" + num2 + "-" + num3

#         Account.all_account += 1

#     def get_account_num(cls):  # class 매소드 (객체접근필요x)
#         print(cls.all_account)  # cls = class

#     def deposit(self, amount):
#         if amount > 1:
#             self.balance += amount

#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount


# k = Account("kim", 100)
# k.deposit(100)  # 100+100=200
# k.withdraw(90)  # 200-90=110
# print(k.balance)  # 110

# 276
import random


class Account:
    all_account = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account = num1 + "-" + num2 + "-" + num3

        Account.all_account += 1

    def get_account_num(cls):  # class 매소드 (객체접근필요x)
        print(cls.all_account)  # cls = class

    def deposit(self, amount):
        if amount > 1:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount

    def display_info(self):
        print(f"은행이름: {self.bank}")
        print(f"예금주: {self.name}")
        print(f"계좌번호: {self.account}")
        print("잔고: ", format(self.balance, ","))

    # print("잔고: ", "{:,}".format(self.balance))


p = Account("파이썬", 10000)
p.display_info()

# 277
# import random


# class Account:
#     all_account = 0
#     deposit_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account = num1 + "-" + num2 + "-" + num3

#         Account.all_account += 1

#     def get_account_num(cls):  # class 매소드 (객체접근필요x)
#         print(cls.all_account)  # cls = class

#     def deposit(self, amount):
#         if amount > 1:
#             self.balance += amount
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:
#                 self.balance = self.balance * 1.01

#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount

#     def display_info(self):
#         print(f"은행이름: {self.bank}")
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account}")
#         print(f"잔고: {self.balance}")


# p = Account("파이썬", 10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(10000)
# p.deposit(5000)
# p.deposit(5000)
# print(p.balance)

# 278
# import random


# class Account:
#     all_account = 0
#     deposit_count = 0

#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account = num1 + "-" + num2 + "-" + num3

#         Account.all_account += 1

#     def get_account_num(cls):  # class 매소드 (객체접근필요x)
#         print(cls.all_account)  # cls = class

#     def deposit(self, amount):
#         if amount > 1:
#             self.balance += amount
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:
#                 self.balance = self.balance * 1.01

#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount

#     def display_info(self):
#         print(f"은행이름: {self.bank}")
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account}")
#         print("잔고: ", format(self.balance, ","))
#         # print("잔고: ", "{:,}".format(self.balance))

# a = Account("전예슬", 1000000)
# b = Account("김", 20000)
# c = Account("이", 20000)
# data = []
# data.append(a)
# data.append(b)
# data.append(c)
# print(data)


# 279
# for c in data:
#     if c.balance >= 1000000:
#         c.display_info()
# 280
# import random


# class Account:
#     all_account = 0

#     def __init__(self, name, balance):

#         self.deposit_count = 0
#         self.deposit_log = []
#         self.withdraw_log = []

#         self.name = name
#         self.balance = balance
#         self.bank = "SC은행"

#         num1 = random.randint(0, 999)
#         num2 = random.randint(0, 99)
#         num3 = random.randint(0, 999999)

#         num1 = str(num1).zfill(3)
#         num2 = str(num2).zfill(2)
#         num3 = str(num3).zfill(6)
#         self.account = num1 + "-" + num2 + "-" + num3

#         Account.all_account += 1

#     def get_account_num(cls):  # class 매소드 (객체접근필요x)
#         print(cls.all_account)  # cls = class

#     def deposit(self, amount):
#         if amount > 1:
#             self.balance += amount
#             self.deposit_log.append(amount)
#             self.deposit_count += 1
#             if self.deposit_count % 5 == 0:
#                 self.balance = self.balance * 1.01

#     def deposit_history(self):
#         print(self.deposit_log)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             self.withdraw_log.append(amount)

#     def withdraw_history(self):
#         print(self.withdraw_log)

#     def display_info(self):
#         print(f"은행이름: {self.bank}")
#         print(f"예금주: {self.name}")
#         print(f"계좌번호: {self.account}")
#         print(f"잔고: {self.balance}")
#         print("잔고: ", format(self.balance, ","))
#         # print("잔고: ", "{:,}".format(self.balance))

# k = Account("Kim", 1000)
# k.deposit(100)
# k.deposit(200)
# k.deposit(300)
# k.deposit_history()

# k.withdraw(100)
# k.withdraw(200)
# k.withdraw_history()
